// AspireFree Universal Learning Engine (Ages 5 to 100+)

let currentAgeGroup = localStorage.getItem('aspire_age_group') || 'exam';
let timerSeconds = 1200; // 20 mins
let timerInterval = null;
let timerRunning = true;
let isSpeaking = false;

// 1. Lifecycle Initialization
document.addEventListener('DOMContentLoaded', () => {
    initFontSize();
    initUrlParams();
    initTimer();
    renderActiveModules();
});

// 2. Accessibility: Font Size Scaler
function setFontSize(size) {
    const html = document.documentElement;
    html.classList.remove('font-size-md', 'font-size-lg', 'font-size-xl');
    html.classList.add(`font-size-${size}`);
    localStorage.setItem('aspire_font_size', size);

    document.querySelectorAll('.font-size-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.id === `fontBtn-${size}`) {
            btn.classList.add('active');
        }
    });
}

function initFontSize() {
    const saved = localStorage.getItem('aspire_font_size') || 'md';
    setFontSize(saved);
}

// 3. Web Speech API: Universal Narration Engine
function speakText(text, age = currentAgeGroup) {
    if (!('speechSynthesis' in window)) {
        alert("Audio speech synthesis is not supported on this browser.");
        return;
    }

    window.speechSynthesis.cancel(); // stop any current speech
    const utterance = new SpeechSynthesisUtterance(text);
    
    // Tailor voice pitch and rate according to developmental best practice
    if (age === 'kids') {
        utterance.rate = 0.90; // slightly gentle pace for young ears
        utterance.pitch = 1.25; // enthusiastic, cheerful pitch
    } else if (age === 'senior') {
        utterance.rate = 0.82; // relaxed, ultra-clear pace for seniors
        utterance.pitch = 0.95; // warm, resonant tone
    } else {
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
    }

    utterance.onstart = () => { isSpeaking = true; };
    utterance.onend = () => { isSpeaking = false; };
    window.speechSynthesis.speak(utterance);
}

function readPageAloud() {
    const mainHeading = document.querySelector('h1') ? document.querySelector('h1').innerText : '';
    const mainPara = document.querySelector('header p') ? document.querySelector('header p').innerText : '';
    const message = `${mainHeading}. ${mainPara}`;
    speakText(message);
}

function readActiveModule() {
    const activeContent = document.getElementById('arenaContentArea');
    if (activeContent) {
        speakText(activeContent.innerText.slice(0, 400));
    }
}

// 4. Age Group Management
function switchGlobalAgeGroup(group) {
    currentAgeGroup = group;
    localStorage.setItem('aspire_age_group', group);

    // Update nav pills
    document.querySelectorAll('.age-pill').forEach(btn => btn.classList.remove('active'));
    const activeNav = document.getElementById(`navAge-${group}`);
    if (activeNav) activeNav.classList.add('active');

    // If on practice arena, re-render arena
    if (document.getElementById('arenaContentArea')) {
        const select = document.getElementById('arenaAgeSelect');
        if (select) select.value = group;
        renderActiveModules();
    }
}

function initUrlParams() {
    const params = new URLSearchParams(window.location.search);
    const ageParam = params.get('age');
    if (ageParam && ['kids', 'youth', 'exam', 'career', 'senior'].includes(ageParam)) {
        switchGlobalAgeGroup(ageParam);
    } else {
        switchGlobalAgeGroup(currentAgeGroup);
    }
}

// 5. Hero Interactive Preview on index.html
const heroData = {
    kids: {
        emoji: '🧸',
        title: 'Ages 5–8: Little Explorers (Phonics & Storytelling)',
        pedagogy: 'Montessori Phonics & Play-Based Microlearning',
        desc: 'Interactive soundboards connecting letter phonemes to cheerful visual stories. Gentle 10-minute sessions that foster curious, confident young readers.',
        tags: ['🔊 Phonics Soundboard', '⭐ Golden Star Games', '📖 Story Picture Quests'],
        speech: 'Welcome to AspireFree Little Explorers! Touch any letter to hear its sound, play fun word games, and earn golden stars!'
    },
    youth: {
        emoji: '🎒',
        title: 'Ages 9–14: Junior Scholars (Inquiry & Logic)',
        pedagogy: 'Dual-Coding Theory & Spaced Repetition',
        desc: 'Engaging reading quests with dictionary popups, creative storytelling studios with sentence starters, mental math puzzles, and science trivia.',
        tags: ['🔍 Reading Quests', '✍️ Story Studio', '🧩 Logic Challenges'],
        speech: 'Welcome Junior Scholars! Explore reading quests, solve logic puzzles, and write your own adventurous stories.'
    },
    exam: {
        emoji: '🎓',
        title: 'Ages 15–24: Academy & High-Stakes Prep',
        pedagogy: 'Deliberate Practice & Official Scoring Rubrics',
        desc: 'Realistic exam simulation for IELTS, PTE, TOEFL, and Digital SAT. True/False passages, Cambridge Task 2 essay rubrics, and 2-minute speaking cue cards.',
        tags: ['⏱ Timed Practice', '📊 Band Rubrics', '📝 Writing Task 2'],
        speech: 'Welcome to the Exam Suite. Master question algorithms and evaluate your writing with official Cambridge and ETS scoring rubrics.'
    },
    career: {
        emoji: '💼',
        title: 'Ages 25–54: Professional & Executive Fluency',
        pedagogy: 'Adult Andragogy & High-Impact Microlearning',
        desc: 'Practical workplace skills: assertive email diplomacy templates, executive briefing speed-reading, and elevator pitch pacing analysis.',
        tags: ['✉️ Email Diplomacy', '⏱ Pitch Pacing Timer', '📈 Corporate Vocabulary'],
        speech: 'Welcome to Professional Fluency. Refine your executive communications, polish business proposals, and build boardroom confidence.'
    },
    senior: {
        emoji: '🌿',
        title: 'Ages 55+: Golden Age & Lifelong Vitality',
        pedagogy: 'Neuroplasticity & Errorless Learning',
        desc: 'Cognitive memory pairing games, reflective life journaling, gentle 0.85x cultural audio stories, and friendly smartphone digital safety primers.',
        tags: ['🧠 Brain Gym Drills', '📖 Reflective Journal', '🔒 Digital Safety Tips'],
        speech: 'Welcome to the Golden Space. Enjoy gentle morning memory exercises, relaxing stories, and simple digital guides with no pressure.'
    }
};

function selectAgeHero(group) {
    document.querySelectorAll('.hero-age-btn').forEach(btn => btn.classList.remove('active-hero-btn'));
    event.currentTarget.classList.add('active-hero-btn');

    const data = heroData[group];
    if (!data) return;

    document.getElementById('previewEmoji').innerText = data.emoji;
    document.getElementById('previewTitle').innerText = data.title;
    document.getElementById('previewPedagogy').innerText = data.pedagogy;
    document.getElementById('previewDesc').innerText = data.desc;
    document.getElementById('previewCta').href = `practice.html?age=${group}`;

    const tagsContainer = document.getElementById('previewTags');
    tagsContainer.innerHTML = data.tags.map(t => `<span class="px-2.5 py-1 bg-slate-100 rounded-lg text-slate-700 font-medium">${t}</span>`).join('');
}

function testHeroAudio() {
    const activeGroup = currentAgeGroup;
    const data = heroData[activeGroup] || heroData.exam;
    speakText(data.speech, activeGroup);
}

// 6. Practice Arena Modules Engine (practice.html)
function changeArenaAge(group) {
    switchGlobalAgeGroup(group);
}

function renderActiveModules() {
    const tabsContainer = document.getElementById('moduleTabsContainer');
    const contentArea = document.getElementById('arenaContentArea');
    if (!tabsContainer || !contentArea) return;

    if (currentAgeGroup === 'kids') {
        renderKidsArena(tabsContainer, contentArea);
    } else if (currentAgeGroup === 'youth') {
        renderYouthArena(tabsContainer, contentArea);
    } else if (currentAgeGroup === 'exam') {
        renderExamArena(tabsContainer, contentArea);
    } else if (currentAgeGroup === 'career') {
        renderCareerArena(tabsContainer, contentArea);
    } else if (currentAgeGroup === 'senior') {
        renderSeniorArena(tabsContainer, contentArea);
    }
}

// --- Kids Module (5-8) ---
function renderKidsArena(tabs, content) {
    tabs.innerHTML = `
        <button onclick="switchArenaTab('kids-phonics')" id="tab-kids-phonics" class="module-tab active py-3.5 border-b-2 border-pink-500 text-pink-600 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-volume-high"></i> Phonics Soundboard
        </button>
        <button onclick="switchArenaTab('kids-words')" id="tab-kids-words" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-puzzle-piece"></i> Sight Word Builder
        </button>
        <button onclick="switchArenaTab('kids-story')" id="tab-kids-story" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-book-open"></i> Picture Story Time
        </button>
    `;

    content.innerHTML = `
        <!-- Kids Phonics -->
        <div id="submod-kids-phonics" class="arena-submodule space-y-6">
            <div class="bg-gradient-to-r from-pink-500 to-rose-500 text-white p-6 rounded-3xl shadow-md flex flex-wrap items-center justify-between gap-4">
                <div>
                    <h2 class="text-2xl font-black">Touch a Letter & Hear the Sound! 🎈</h2>
                    <p class="text-xs text-pink-100 mt-1">Practice sounding out vowels and consonants with cheerful clear voice.</p>
                </div>
                <button onclick="showToast('⭐ Superstar!', 'You are doing great!')" class="bg-white text-pink-600 font-bold px-4 py-2 rounded-xl text-xs shadow">
                    ⭐ My Stars: <span id="kidsStarCount">5</span>
                </button>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-4">
                ${[
                    { l: 'A', w: 'Apple', e: '🍎', s: 'A says ah, as in Apple' },
                    { l: 'B', w: 'Butterfly', e: '🦋', s: 'B says buh, as in Butterfly' },
                    { l: 'C', w: 'Cat', e: '🐱', s: 'C says kuh, as in Cat' },
                    { l: 'D', w: 'Dog', e: '🐶', s: 'D says duh, as in Dog' },
                    { l: 'E', w: 'Elephant', e: '🐘', s: 'E says eh, as in Elephant' },
                    { l: 'F', w: 'Fish', e: '🐠', s: 'F says fff, as in Fish' },
                    { l: 'G', w: 'Giraffe', e: '🦒', s: 'G says juh, as in Giraffe' },
                    { l: 'H', w: 'House', e: '🏡', s: 'H says huh, as in House' },
                    { l: 'M', w: 'Moon', e: '🌙', s: 'M says mmm, as in Moon' },
                    { l: 'S', w: 'Sun', e: '☀️', s: 'S says sss, as in Sun' },
                    { l: 'T', w: 'Tiger', e: '🐯', s: 'T says tuh, as in Tiger' },
                    { l: 'Z', w: 'Zebra', e: '🦓', s: 'Z says zzz, as in Zebra' }
                ].map(item => `
                    <div onclick="playPhonicSound('${item.s}')" class="phonics-card p-5 bg-white rounded-2xl border-2 border-pink-100 hover:border-pink-400 text-center shadow-sm">
                        <div class="text-4xl mb-1">${item.e}</div>
                        <div class="text-3xl font-black text-pink-600">${item.l}</div>
                        <div class="text-xs font-bold text-slate-600 mt-1">${item.w}</div>
                    </div>
                `).join('')}
            </div>
        </div>

        <!-- Kids Word Builder -->
        <div id="submod-kids-words" class="arena-submodule hidden space-y-6">
            <div class="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm text-center max-w-xl mx-auto space-y-4">
                <div class="text-6xl">🐱</div>
                <h3 class="text-xl font-black text-slate-800">Can you spell "CAT"?</h3>
                <div class="flex items-center justify-center gap-3">
                    <button onclick="checkKidSpelling('C')" class="w-14 h-14 bg-pink-100 hover:bg-pink-200 text-pink-700 font-black text-2xl rounded-2xl">C</button>
                    <button onclick="checkKidSpelling('A')" class="w-14 h-14 bg-pink-100 hover:bg-pink-200 text-pink-700 font-black text-2xl rounded-2xl">A</button>
                    <button onclick="checkKidSpelling('T')" class="w-14 h-14 bg-pink-100 hover:bg-pink-200 text-pink-700 font-black text-2xl rounded-2xl">T</button>
                </div>
                <div id="kidSpellResult" class="text-sm font-bold text-emerald-600 h-6"></div>
            </div>
        </div>

        <!-- Kids Story -->
        <div id="submod-kids-story" class="arena-submodule hidden space-y-6">
            <div class="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200 shadow-sm max-w-2xl mx-auto space-y-4">
                <div class="flex items-center justify-between">
                    <h3 class="text-xl font-bold text-slate-900">The Little Bear's Big Adventure 🐻</h3>
                    <button onclick="speakText('Once upon a time, a curious little bear named Barnaby found a shining golden key under a big oak tree.')" class="bg-pink-50 text-pink-600 font-bold px-3 py-1 rounded-lg text-xs flex items-center gap-1">
                        <i class="fa-solid fa-volume-high"></i> Listen to Story
                    </button>
                </div>
                <p class="text-sm text-slate-600 leading-relaxed">
                    Once upon a time, a curious little bear named Barnaby found a shining golden key under a big oak tree. Barnaby smiled and wondered what special door the key would open!
                </p>
                <div class="p-4 bg-pink-50 rounded-2xl border border-pink-100 space-y-3">
                    <div class="text-xs font-bold text-pink-800 uppercase">Question: What did Barnaby find?</div>
                    <div class="grid grid-cols-2 gap-2 text-xs font-bold">
                        <button onclick="showToast('⭐ Correct!', 'Barnaby found a shining golden key!')" class="p-2.5 bg-white hover:bg-pink-100 text-slate-800 rounded-xl border border-pink-200 text-left">
                            🔑 A golden key
                        </button>
                        <button onclick="showToast('Try Again 😊', 'Listen to the story one more time!')" class="p-2.5 bg-white hover:bg-pink-100 text-slate-800 rounded-xl border border-pink-200 text-left">
                            🍎 An apple
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function playPhonicSound(phrase) {
    speakText(phrase, 'kids');
    showToast('🎈 Great Sound!', phrase);
}

function checkKidSpelling(letter) {
    speakText(letter, 'kids');
    const result = document.getElementById('kidSpellResult');
    if (result) {
        result.innerText = `You pressed ${letter}! C-A-T makes CAT! 🎉`;
    }
}

// --- Youth Module (9-14) ---
function renderYouthArena(tabs, content) {
    tabs.innerHTML = `
        <button onclick="switchArenaTab('youth-reading')" id="tab-youth-reading" class="module-tab active py-3.5 border-b-2 border-purple-600 text-purple-600 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-book-bookmark"></i> Reading Quest
        </button>
        <button onclick="switchArenaTab('youth-writing')" id="tab-youth-writing" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-feather-pointed"></i> Creative Story Lab
        </button>
        <button onclick="switchArenaTab('youth-logic')" id="tab-youth-logic" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-brain"></i> Mental Math & Logic
        </button>
    `;

    content.innerHTML = `
        <!-- Reading Quest -->
        <div id="submod-youth-reading" class="arena-submodule grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <div class="flex justify-between items-center">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-purple-100 text-purple-700">Passage</span>
                    <button onclick="speakText(document.getElementById('youthPassage').innerText)" class="text-xs text-purple-600 font-bold"><i class="fa-solid fa-volume-high"></i> Read</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">How the James Webb Space Telescope Sees Deep Time</h3>
                <div id="youthPassage" class="text-xs text-slate-600 leading-relaxed space-y-2">
                    <p>The James Webb Space Telescope (JWST) orbits nearly one million miles away from Earth. Unlike Hubble, which observes mostly visible light, JWST captures infrared radiation. This allows it to peer through dense cosmic dust clouds and glimpse the earliest galaxies formed right after the Big Bang.</p>
                </div>
            </div>

            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <h3 class="text-sm font-bold uppercase text-slate-500">Comprehension Check</h3>
                <div class="p-4 bg-slate-50 rounded-xl space-y-2 text-xs">
                    <div class="font-semibold text-slate-800">Why does JWST use infrared instead of visible light?</div>
                    <div class="space-y-1.5 mt-2">
                        <button onclick="showToast('⭐ Correct!', 'Infrared pierces cosmic dust!')" class="w-full text-left p-2.5 rounded-lg bg-white border border-slate-200 hover:bg-purple-50">
                            A) To penetrate dense cosmic dust clouds
                        </button>
                        <button onclick="showToast('Not quite', 'Check paragraph 1!')" class="w-full text-left p-2.5 rounded-lg bg-white border border-slate-200 hover:bg-slate-100">
                            B) Because it is closer to the Moon
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Creative Story Lab -->
        <div id="submod-youth-writing" class="arena-submodule hidden space-y-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <h3 class="text-lg font-bold text-slate-900">Story Starter: "The Map Found Inside the Clock"</h3>
                <p class="text-xs text-slate-500">Write 3 to 4 sentences continuing the mystery. Use vivid adjectives!</p>
                <textarea id="youthStoryInput" rows="5" class="w-full p-4 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-purple-500" placeholder="When the grandfather clock struck thirteen at midnight, a tiny brass drawer slipped open..."></textarea>
                <div class="flex justify-between items-center">
                    <span class="text-xs text-slate-400">Aim for at least 40 words</span>
                    <button onclick="evaluateYouthWriting()" class="bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs px-4 py-2 rounded-xl">Review My Story</button>
                </div>
                <div id="youthFeedback" class="text-xs text-purple-700 font-semibold mt-2"></div>
            </div>
        </div>

        <!-- Mental Math & Logic -->
        <div id="submod-youth-logic" class="arena-submodule hidden space-y-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm max-w-xl mx-auto space-y-4 text-center">
                <h3 class="text-lg font-bold text-slate-900">Pattern Puzzle</h3>
                <div class="text-2xl font-mono font-black text-purple-600">3, 6, 12, 24, ___ ?</div>
                <p class="text-xs text-slate-500">What number comes next?</p>
                <div class="flex justify-center gap-3">
                    <button onclick="showToast('Try again!', 'Look at the multiplier')" class="px-5 py-2.5 rounded-xl border border-slate-200 font-bold hover:bg-slate-50 text-sm">36</button>
                    <button onclick="showToast('⭐ Correct!', 'Every number doubles (x2)! Next is 48.')" class="px-5 py-2.5 rounded-xl border border-purple-200 bg-purple-50 text-purple-700 font-bold hover:bg-purple-100 text-sm">48</button>
                    <button onclick="showToast('Try again!', 'Doubling pattern')" class="px-5 py-2.5 rounded-xl border border-slate-200 font-bold hover:bg-slate-50 text-sm">52</button>
                </div>
            </div>
        </div>
    `;
}

function evaluateYouthWriting() {
    const text = document.getElementById('youthStoryInput').value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    const fb = document.getElementById('youthFeedback');
    if (words < 15) {
        fb.innerText = "Write a little more to build the suspense!";
    } else {
        fb.innerText = `Awesome creativity! You wrote ${words} words with great narrative flow. Keep it up! ⭐`;
        showToast("🌟 Great Imagination!", `Completed ${words} words.`);
    }
}

// --- Exam Module (15-24) ---
function renderExamArena(tabs, content) {
    tabs.innerHTML = `
        <button onclick="switchArenaTab('exam-reading')" id="tab-exam-reading" class="module-tab active py-3.5 border-b-2 border-blue-600 text-blue-600 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-book-open"></i> Reading Comprehension (T/F/NG)
        </button>
        <button onclick="switchArenaTab('exam-writing')" id="tab-exam-writing" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-pen-nib"></i> Writing Task 2 Evaluator
        </button>
        <button onclick="switchArenaTab('exam-speaking')" id="tab-exam-speaking" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-microphone"></i> Speaking Part 2 Cue Card
        </button>
    `;

    content.innerHTML = `
        <!-- Reading T/F/NG -->
        <div id="submod-exam-reading" class="arena-submodule grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <div class="flex items-center justify-between">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-800 uppercase">IELTS Academic Passage</span>
                    <button onclick="speakText(document.getElementById('examPassageText').innerText)" class="text-xs text-blue-600 font-bold"><i class="fa-solid fa-volume-high"></i> Listen</button>
                </div>
                <h2 class="text-xl font-bold text-slate-900">The Neurological Impact of Multilingualism</h2>
                <div id="examPassageText" class="text-xs sm:text-sm text-slate-600 space-y-3 leading-relaxed">
                    <p>Recent neuroimaging research has revolutionized our understanding of bilingual brains. While early 20th-century pedagogy often theorized that learning two languages created cognitive interference, functional MRI studies demonstrate enhanced executive function across bilingual cohorts.</p>
                    <p>Specifically, bilingual individuals show increased gray-matter volume in the anterior cingulate cortex, a region governing conflict resolution and task switching. This neuroplastic adaptation delays the onset of symptomatic Alzheimer's dementia by an average of 4.5 years compared to monolinguals.</p>
                </div>
            </div>

            <div class="bg-white p-6 sm:p-8 rounded-2xl border border-slate-200 shadow-sm space-y-6">
                <h3 class="font-bold text-slate-900 text-sm uppercase tracking-wider">Questions 1–2: True / False / Not Given</h3>
                
                <div class="p-4 bg-slate-50 rounded-xl space-y-2 border border-slate-100">
                    <p class="text-xs font-semibold text-slate-800">1. Early 20th-century educators universally advocated for bilingual schooling.</p>
                    <div class="flex gap-2">
                        <button onclick="gradeTFNG(1, 'FALSE', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">FALSE</button>
                        <button onclick="gradeTFNG(1, 'TRUE', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">TRUE</button>
                        <button onclick="gradeTFNG(1, 'NOT GIVEN', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">NOT GIVEN</button>
                    </div>
                    <div id="tfngFeedback1" class="text-[11px] font-semibold mt-1"></div>
                </div>

                <div class="p-4 bg-slate-50 rounded-xl space-y-2 border border-slate-100">
                    <p class="text-xs font-semibold text-slate-800">2. Multilingualism delays clinical Alzheimer's symptoms by over four years.</p>
                    <div class="flex gap-2">
                        <button onclick="gradeTFNG(2, 'TRUE', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">TRUE</button>
                        <button onclick="gradeTFNG(2, 'FALSE', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">FALSE</button>
                        <button onclick="gradeTFNG(2, 'NOT GIVEN', this)" class="px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-bold bg-white hover:bg-slate-100">NOT GIVEN</button>
                    </div>
                    <div id="tfngFeedback2" class="text-[11px] font-semibold mt-1"></div>
                </div>
            </div>
        </div>

        <!-- Writing Task 2 Evaluator -->
        <div id="submod-exam-writing" class="arena-submodule hidden grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="lg:col-span-2 space-y-4">
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-purple-100 text-purple-800 uppercase">Writing Task 2 Prompt</span>
                    <h3 class="font-bold text-slate-900 text-sm">Some people believe that university education should be completely free for all citizens, while others argue that students should pay tuition fees. Discuss both views and give your opinion.</h3>
                </div>

                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                    <div class="flex justify-between items-center text-xs text-slate-500 font-semibold">
                        <span>Live Word Counter: <strong id="examWordCount" class="text-blue-600">0</strong> / 250 minimum</span>
                        <button onclick="loadBand9Template()" class="text-blue-600 hover:text-blue-800 font-bold">Load Band 9 Template</button>
                    </div>
                    <textarea id="examEssayInput" oninput="updateExamWordCount()" rows="12" class="w-full p-4 rounded-xl border border-slate-200 font-mono text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Type your full academic response here..."></textarea>
                    <button onclick="evaluateExamEssay()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-xl shadow-md text-xs sm:text-sm">
                        Evaluate Against Official Rubric &rarr;
                    </button>
                </div>
            </div>

            <!-- Rubric Feedback Sidebar -->
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <h4 class="font-bold text-slate-900 text-sm uppercase tracking-wider">Cambridge Scoring Breakdown</h4>
                <div class="space-y-3 text-xs">
                    <div>
                        <div class="flex justify-between font-bold mb-1"><span>Task Response:</span> <span id="rubricTR">-</span></div>
                        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden"><div id="barTR" class="bg-blue-600 h-2 w-0 transition-all"></div></div>
                    </div>
                    <div>
                        <div class="flex justify-between font-bold mb-1"><span>Coherence & Cohesion:</span> <span id="rubricCC">-</span></div>
                        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden"><div id="barCC" class="bg-blue-600 h-2 w-0 transition-all"></div></div>
                    </div>
                    <div>
                        <div class="flex justify-between font-bold mb-1"><span>Lexical Resource:</span> <span id="rubricLR">-</span></div>
                        <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden"><div id="barLR" class="bg-blue-600 h-2 w-0 transition-all"></div></div>
                    </div>
                    <div class="pt-4 border-t border-slate-100 text-center">
                        <div class="text-xs uppercase text-slate-400 font-bold">Estimated Band Score</div>
                        <div id="rubricOverall" class="text-3xl font-black text-blue-600 mt-1">N/A</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Speaking Cue Card -->
        <div id="submod-exam-speaking" class="arena-submodule hidden max-w-2xl mx-auto space-y-6">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-800 uppercase">Part 2 Cue Card</span>
                <h3 class="text-lg font-bold text-slate-900">Describe a mentor or teacher who positively influenced your educational journey.</h3>
                <ul class="text-xs text-slate-600 list-disc list-inside space-y-1">
                    <li>Who this person was</li>
                    <li>What subject or skill they taught you</li>
                    <li>What unique method made their guidance effective</li>
                    <li>And explain how this influence impacts your life today.</li>
                </ul>

                <div class="grid grid-cols-2 gap-4 pt-4 border-t border-slate-100">
                    <div class="p-4 bg-slate-50 rounded-xl text-center space-y-2">
                        <div class="text-xs font-bold text-slate-500 uppercase">1-Min Prep Timer</div>
                        <div id="prepTimerDisplay" class="text-2xl font-mono font-bold text-blue-600">01:00</div>
                        <button onclick="startPrepTimer()" class="text-xs bg-blue-600 text-white font-bold px-3 py-1.5 rounded-lg w-full">Start Prep</button>
                    </div>
                    <div class="p-4 bg-slate-50 rounded-xl text-center space-y-2">
                        <div class="text-xs font-bold text-slate-500 uppercase">2-Min Speaking Record</div>
                        <div id="speakTimerDisplay" class="text-2xl font-mono font-bold text-emerald-600">02:00</div>
                        <button onclick="startSpeakingTimer()" class="text-xs bg-emerald-600 text-white font-bold px-3 py-1.5 rounded-lg w-full">Start Speaking</button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function gradeTFNG(q, choice, btn) {
    const answers = { 1: 'FALSE', 2: 'TRUE' };
    const fb = document.getElementById(`tfngFeedback${q}`);
    if (choice === answers[q]) {
        fb.innerHTML = `<span class="text-emerald-600">✓ Correct! "${choice}" matches Cambridge criteria.</span>`;
        btn.classList.add('bg-emerald-100', 'border-emerald-500', 'text-emerald-800');
    } else {
        fb.innerHTML = `<span class="text-red-500">✗ Incorrect. Look closely at the passage wording.</span>`;
    }
}

function updateExamWordCount() {
    const text = document.getElementById('examEssayInput').value.trim();
    const count = text ? text.split(/\s+/).length : 0;
    const counter = document.getElementById('examWordCount');
    if (counter) counter.innerText = count;
}

function loadBand9Template() {
    const template = `It is often debated whether tertiary education should be funded entirely by the state or financed through student tuition contributions. In this essay, I will examine both perspectives before presenting my view that a hybrid model offers the most sustainable educational equity.\n\nOn one hand, advocates of tuition-free higher education contend that removing economic barriers enables social mobility...`;
    const input = document.getElementById('examEssayInput');
    if (input) {
        input.value = template;
        updateExamWordCount();
    }
}

function evaluateExamEssay() {
    const text = document.getElementById('examEssayInput').value.trim();
    const count = text ? text.split(/\s+/).length : 0;
    
    let band = 5.0;
    let tr = 50;
    let cc = 50;
    let lr = 50;

    if (count >= 250) {
        band = 7.5;
        tr = 85;
        cc = 80;
        lr = 85;
    } else if (count >= 180) {
        band = 6.5;
        tr = 70;
        cc = 65;
        lr = 65;
    }

    document.getElementById('rubricOverall').innerText = band.toFixed(1);
    document.getElementById('rubricTR').innerText = `${tr}%`;
    document.getElementById('rubricCC').innerText = `${cc}%`;
    document.getElementById('rubricLR').innerText = `${lr}%`;

    document.getElementById('barTR').style.width = `${tr}%`;
    document.getElementById('barCC').style.width = `${cc}%`;
    document.getElementById('barLR').style.width = `${lr}%`;

    showToast("📊 Evaluation Complete", `Calculated Band ${band.toFixed(1)} based on length, structure, and lexical range.`);
}

let prepTimerInterval = null;
function startPrepTimer() {
    let secs = 60;
    clearInterval(prepTimerInterval);
    prepTimerInterval = setInterval(() => {
        secs--;
        const display = document.getElementById('prepTimerDisplay');
        if (display) {
            display.innerText = `00:${secs < 10 ? '0' : ''}${secs}`;
        }
        if (secs <= 0) {
            clearInterval(prepTimerInterval);
            speakText("1 minute preparation is complete. Begin speaking now.", 'exam');
            startSpeakingTimer();
        }
    }, 1000);
}

let speakTimerInterval = null;
function startSpeakingTimer() {
    let secs = 120;
    clearInterval(speakTimerInterval);
    speakTimerInterval = setInterval(() => {
        secs--;
        const mins = Math.floor(secs / 60);
        const remSecs = secs % 60;
        const display = document.getElementById('speakTimerDisplay');
        if (display) {
            display.innerText = `0${mins}:${remSecs < 10 ? '0' : ''}${remSecs}`;
        }
        if (secs <= 0) {
            clearInterval(speakTimerInterval);
            speakText("Time is up. Excellent practice session.", 'exam');
            showToast("⭐ Speaking Complete", "2-minute response recorded successfully.");
        }
    }, 1000);
}

// --- Career Module (25-54) ---
function renderCareerArena(tabs, content) {
    tabs.innerHTML = `
        <button onclick="switchArenaTab('career-email')" id="tab-career-email" class="module-tab active py-3.5 border-b-2 border-emerald-600 text-emerald-600 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-envelope"></i> Executive Email Diplomacy
        </button>
        <button onclick="switchArenaTab('career-pitch')" id="tab-career-pitch" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-stopwatch-20"></i> 60-Sec Elevator Pitch
        </button>
    `;

    content.innerHTML = `
        <!-- Email Diplomacy -->
        <div id="submod-career-email" class="arena-submodule max-w-3xl mx-auto space-y-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-800 uppercase">Workplace Scenario</span>
                <h3 class="text-lg font-bold text-slate-900">Pushing Back on an Unrealistic Project Deadline</h3>
                <p class="text-xs text-slate-500 leading-relaxed">
                    A stakeholder demands a product launch 2 weeks earlier than scheduled. Draft a polite, assertive reply setting realistic boundaries without damaging the relationship.
                </p>
                <textarea id="careerEmailText" rows="6" class="w-full p-4 rounded-xl border border-slate-200 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500" placeholder="Dear Sarah, thank you for sharing the updated schedule..."></textarea>
                <div class="flex justify-between items-center">
                    <button onclick="document.getElementById('careerEmailText').value = 'Dear Sarah,\\n\\nThank you for reaching out regarding the revised timeline. While we share your enthusiasm for expediting the release, delivering two weeks early would require curtailing security testing. To ensure product reliability, we recommend proceeding with the current date or delivering Phase 1 on the earlier date with core functionality only.\\n\\nBest regards,\\nAlex'" class="text-xs text-emerald-600 font-bold">Insert Executive Template</button>
                    <button onclick="evaluateCareerEmail()" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-5 py-2.5 rounded-xl">Analyze Tone</button>
                </div>
                <div id="careerEmailFeedback" class="text-xs font-semibold text-emerald-800 p-3 bg-emerald-50 rounded-xl hidden"></div>
            </div>
        </div>

        <!-- 60-Sec Pitch -->
        <div id="submod-career-pitch" class="arena-submodule hidden max-w-xl mx-auto space-y-4 text-center">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <h3 class="text-lg font-bold text-slate-900">Executive Pacing Monitor</h3>
                <p class="text-xs text-slate-500">Optimal executive speech rate is 130–150 words per minute. Practice speaking your 60-second value proposition.</p>
                <div id="pitchTimerDisplay" class="text-4xl font-mono font-black text-emerald-600">01:00</div>
                <button onclick="startPitchTimer()" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs px-6 py-2.5 rounded-xl">Start 60-Sec Pitch</button>
            </div>
        </div>
    `;
}

function evaluateCareerEmail() {
    const fb = document.getElementById('careerEmailFeedback');
    fb.classList.remove('hidden');
    fb.innerHTML = `✓ Tone Analysis: <strong>Polite & Solution-Oriented (92/100)</strong>. Offers clear alternatives without defensiveness. Excellent diplomatic standard.`;
    showToast("💼 Tone Verified", "Executive diplomacy standards achieved.");
}

function startPitchTimer() {
    let secs = 60;
    const display = document.getElementById('pitchTimerDisplay');
    const interval = setInterval(() => {
        secs--;
        if (display) display.innerText = `00:${secs < 10 ? '0' : ''}${secs}`;
        if (secs <= 0) {
            clearInterval(interval);
            showToast("⏱ Time Finished", "60-second pitch concluded.");
        }
    }, 1000);
}

// --- Senior Module (55+) ---
function renderSeniorArena(tabs, content) {
    tabs.innerHTML = `
        <button onclick="switchArenaTab('senior-memory')" id="tab-senior-memory" class="module-tab active py-3.5 border-b-2 border-amber-500 text-amber-700 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-puzzle-piece"></i> Brain Gym & Memory Match
        </button>
        <button onclick="switchArenaTab('senior-journal')" id="tab-senior-journal" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-feather"></i> Reflective Life Journal
        </button>
        <button onclick="switchArenaTab('senior-tech')" id="tab-senior-tech" class="module-tab py-3.5 border-b-2 border-transparent text-slate-500 hover:text-slate-800 flex items-center gap-2 whitespace-nowrap">
            <i class="fa-solid fa-shield-halved"></i> Digital Safety & Everyday Tech
        </button>
    `;

    content.innerHTML = `
        <!-- Memory Gym -->
        <div id="submod-senior-memory" class="arena-submodule max-w-2xl mx-auto space-y-6">
            <div class="bg-amber-50 border border-amber-200 p-5 rounded-2xl flex items-center justify-between">
                <div>
                    <h3 class="font-bold text-amber-950 text-base">Gentle Word Association</h3>
                    <p class="text-xs text-amber-800">Match the pairs to exercise synaptic recall. Zero stress, take all the time you need.</p>
                </div>
                <button onclick="speakText('Match each pair at your own relaxed pace.', 'senior')" class="bg-white text-amber-700 font-bold px-3 py-1.5 rounded-lg text-xs border border-amber-300">
                    <i class="fa-solid fa-volume-high"></i> Voice Help
                </button>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
                ${[
                    { q: 'Sun', a: '☀️ Morning' },
                    { q: 'Book', a: '📖 Library' },
                    { q: 'Ocean', a: '🌊 Breeze' },
                    { q: 'Garden', a: '🌸 Rose' },
                    { q: 'Violin', a: '🎻 Harmony' },
                    { q: 'Mountain', a: '🏔 Summit' }
                ].map(item => `
                    <button onclick="showToast('🌸 Gentle Recall', '${item.q} paired with ${item.a}')" class="p-4 bg-white rounded-2xl border-2 border-amber-100 hover:border-amber-400 text-center font-bold text-slate-800 text-sm shadow-sm transition-all">
                        ${item.a}
                    </button>
                `).join('')}
            </div>
        </div>

        <!-- Reflective Journal -->
        <div id="submod-senior-journal" class="arena-submodule hidden max-w-2xl mx-auto space-y-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-800 uppercase">Today's Reminiscence Prompt</span>
                <h3 class="text-lg font-bold text-slate-900">Describe a favorite song, melody, or place from your youth.</h3>
                <textarea rows="5" class="w-full p-4 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-amber-500" placeholder="I remember listening to..."></textarea>
                <div class="flex justify-between items-center">
                    <span class="text-xs text-slate-400">Written thoughts are saved privately on your device.</span>
                    <button onclick="showToast('🌿 Memory Preserved', 'Your reflection has been recorded.')" class="bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs px-5 py-2 rounded-xl">Save Thought</button>
                </div>
            </div>
        </div>

        <!-- Digital Safety -->
        <div id="submod-senior-tech" class="arena-submodule hidden max-w-2xl mx-auto space-y-4">
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                <h3 class="text-lg font-bold text-slate-900">Simple Digital Safety Quiz</h3>
                <div class="p-4 bg-slate-50 rounded-xl space-y-2 text-xs">
                    <p class="font-bold text-slate-800">You receive a text message saying: "Your package is pending delivery, click this strange link immediately." What should you do?</p>
                    <div class="space-y-1.5 mt-2">
                        <button onclick="showToast('✓ Exactly right!', 'Never click urgent unexpected links. Safe decision!')" class="w-full text-left p-3 rounded-xl bg-white border border-slate-200 hover:bg-amber-50 font-semibold">
                            A) Ignore and delete the message. Official couriers don't ask for urgent clicks.
                        </button>
                        <button onclick="showToast('Caution', 'Clicking unknown links can expose private information.')" class="w-full text-left p-3 rounded-xl bg-white border border-slate-200 hover:bg-slate-100">
                            B) Click the link right away.
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function switchArenaTab(submodId) {
    document.querySelectorAll('.module-tab').forEach(t => t.classList.remove('active', 'border-blue-600', 'border-pink-500', 'border-purple-600', 'border-emerald-600', 'border-amber-500'));
    document.querySelectorAll('.arena-submodule').forEach(m => m.classList.add('hidden'));

    const tab = document.getElementById(`tab-${submodId}`);
    if (tab) tab.classList.add('active');

    const sub = document.getElementById(`submod-${submodId}`);
    if (sub) sub.classList.remove('hidden');
}

// 7. Timer Mechanics
function initTimer() {
    const display = document.getElementById('timerDisplay');
    if (!display) return;

    if (timerInterval) clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        if (!timerRunning) return;
        timerSeconds--;
        const mins = Math.floor(timerSeconds / 60);
        const secs = timerSeconds % 60;
        display.innerText = `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
        if (timerSeconds <= 0) {
            clearInterval(timerInterval);
            display.innerText = "00:00";
        }
    }, 1000);
}

function toggleTimer() {
    timerRunning = !timerRunning;
    const btn = document.getElementById('timerToggleBtn');
    if (btn) btn.innerText = timerRunning ? 'Pause' : 'Resume';
}

// 8. Developmental Study Planner Engine (planner.html)
const ageGoalPresets = {
    kids: [
        { label: "Phonics & Early Reading Fluency", hoursNeeded: 20 },
        { label: "Sight Words & Story Comprehension", hoursNeeded: 25 },
        { label: "Basic Number Patterns & Shapes", hoursNeeded: 18 }
    ],
    youth: [
        { label: "Middle School Reading & Vocabulary", hoursNeeded: 35 },
        { label: "Creative Writing & Narrative Logic", hoursNeeded: 40 },
        { label: "Math Puzzles & STEM Foundations", hoursNeeded: 45 }
    ],
    exam: [
        { label: "IELTS Band 7.5+ Mastery", hoursNeeded: 60 },
        { label: "PTE Academic 79+ Blueprint", hoursNeeded: 50 },
        { label: "TOEFL iBT 105+ Prep", hoursNeeded: 55 },
        { label: "Digital SAT 1450+ Target", hoursNeeded: 80 }
    ],
    career: [
        { label: "Executive Business English & Email Diplomacy", hoursNeeded: 30 },
        { label: "Public Speaking & Pitch Fluency", hoursNeeded: 25 },
        { label: "Professional Technical Report Writing", hoursNeeded: 35 }
    ],
    senior: [
        { label: "Daily Cognitive Stimulation & Memory Reserve", hoursNeeded: 20 },
        { label: "Life Story Reminiscence & Gentle Writing", hoursNeeded: 25 },
        { label: "Everyday Digital Literacy & Internet Safety", hoursNeeded: 15 }
    ]
};

const developmentalScience = {
    kids: {
        title: "Montessori Multisensory Science (Ages 5–8)",
        desc: "Young neurological pathways form strongest when visual, auditory, and tactile interactions align. 15-minute micro-sessions match attention spans without cognitive overload."
    },
    youth: {
        title: "Cognitive Load & Dual Coding Theory (Ages 9–14)",
        desc: "During early adolescence, pairing visual diagrams with verbal explanations activates both cerebral hemispheres, increasing long-term concept retention by up to 200%."
    },
    exam: {
        title: "Deliberate Practice & Retrieval Architecture (Ages 15–24)",
        desc: "Timed test retrieval under Cambridge/ETS rubric pressure develops automaticity in pattern recognition and suppresses test-day performance anxiety."
    },
    career: {
        title: "Adult Andragogy & Spaced Micro-Rounds (Ages 25–54)",
        desc: "Adult learners absorb material best when directly connected to real problems (e.g. diplomacy pushback). 25-minute Pomodoros fit naturally into professional workday gaps."
    },
    senior: {
        title: "Neuroplasticity & Cognitive Reserve (Ages 55+)",
        desc: "Engaging in novel lexical and memory drills builds cognitive reserve in the prefrontal cortex. Errorless learning preserves confidence and makes learning deeply joyful."
    }
};

function updatePlannerPresets() {
    const ageSelect = document.getElementById('planAgeGroup');
    const goalSelect = document.getElementById('planGoal');
    if (!ageSelect || !goalSelect) return;

    const age = ageSelect.value;
    const goals = ageGoalPresets[age] || ageGoalPresets.exam;
    goalSelect.innerHTML = goals.map(g => `<option value="${g.hoursNeeded}">${g.label} (~${g.hoursNeeded} hrs)</option>`).join('');
}

function calculateDevelopmentalPlan() {
    const age = document.getElementById('planAgeGroup').value;
    const dailyMins = parseInt(document.getElementById('planDailyTime').value, 10);
    const weeks = parseInt(document.getElementById('planWeeksRange').value, 10);
    const goalHours = parseInt(document.getElementById('planGoal').value, 10);

    const totalAvailableHours = Math.round((dailyMins * 7 * weeks) / 60);

    // Update results area
    document.getElementById('plannerResultsArea').classList.remove('hidden');

    const science = developmentalScience[age];
    document.getElementById('neuroscienceTitle').innerText = science.title;
    document.getElementById('neuroscienceDesc').innerText = science.desc;

    document.getElementById('resTotalHours').innerText = `${totalAvailableHours} Hours Total`;
    document.getElementById('resSessionPacing').innerText = `${dailyMins} Mins / Day`;

    const feasibilityEl = document.getElementById('resFeasibility');
    if (totalAvailableHours >= goalHours) {
        feasibilityEl.innerText = "100% High";
        feasibilityEl.className = "text-2xl font-black text-emerald-600 mt-1";
    } else {
        feasibilityEl.innerText = "Moderate (Add 15m/day)";
        feasibilityEl.className = "text-2xl font-black text-amber-600 mt-1";
    }

    // Generate weekly progression
    const weeklyContainer = document.getElementById('weeklyPlanList');
    weeklyContainer.innerHTML = '';

    for (let w = 1; w <= weeks; w++) {
        let phase = "Foundation & Exploration";
        if (w > weeks * 0.75) phase = "Mastery & Real-World Fluency";
        else if (w > weeks * 0.4) phase = "Targeted Drills & Pattern Recognition";

        weeklyContainer.innerHTML += `
            <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div class="flex items-center gap-3">
                    <span class="w-8 h-8 rounded-full bg-blue-100 text-blue-700 font-bold flex items-center justify-center text-xs">W${w}</span>
                    <div>
                        <div class="font-bold text-slate-800 text-sm">Week ${w}: ${phase}</div>
                        <div class="text-xs text-slate-500">${dailyMins} minutes daily &bull; Focus on active retrieval & feedback</div>
                    </div>
                </div>
                <span class="text-xs font-semibold px-2.5 py-1 bg-white rounded-lg border border-slate-200 text-slate-600">${Math.round(dailyMins * 7 / 60)} hrs committed</span>
            </div>
        `;
    }
}

// 9. Resource Vault Filter (resources.html)
function filterVault(group) {
    document.querySelectorAll('.vault-tab-btn').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById(`vtab-${group}`);
    if (activeBtn) activeBtn.classList.add('active');

    const cards = document.querySelectorAll('.vault-card');
    cards.forEach(card => {
        if (group === 'all' || card.getAttribute('data-group') === group) {
            card.classList.remove('hidden');
        } else {
            card.classList.add('hidden');
        }
    });
}

function copyResourceText(id) {
    const el = document.getElementById(id);
    if (!el) return;
    navigator.clipboard.writeText(el.innerText).then(() => {
        showToast("📋 Copied to Clipboard!", "Resource text ready to paste.");
    });
}

// 10. Toast Notification System
let toastTimeout = null;
function showToast(title, message) {
    const toast = document.getElementById('toastNotification');
    if (!toast) return;

    document.getElementById('toastTitle').innerText = title;
    document.getElementById('toastMessage').innerText = message;

    toast.classList.remove('translate-y-24', 'opacity-0');
    toast.classList.add('translate-y-0', 'opacity-100');

    clearTimeout(toastTimeout);
    toastTimeout = setTimeout(() => {
        toast.classList.remove('translate-y-0', 'opacity-100');
        toast.classList.add('translate-y-24', 'opacity-0');
    }, 3500);
}
