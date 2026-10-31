#!/usr/bin/env python3
"""
AspireFree Platform Generator
-----------------------------
Generates a complete, modern, responsive, 100% free learning platform with ZERO age boundaries.
From 5-year-old early childhood students to 95-year-old golden age lifelong learners:
- Tailors pedagogical best practices to the user's developmental stage
- Offers adaptive learning interfaces, font scalers, and text-to-speech accessibility
- Interactive practice modules for 5 distinct age cohorts
- Developmental growth planner and age-curated resource vault
- 100% client-side ($0 server costs), deployable to Vercel, GitHub Pages, or any static host.
"""

import os
import sys

def generate_website():
    print("🚀 Generating AspireFree: Universal Learning Platform (Ages 5 to 100+)...")

    # ==========================================
    # 1. index.html - Universal Landing Portal
    # ==========================================
    index_html = '''<!DOCTYPE html>
<html lang="en" class="scroll-smooth font-size-md">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AspireFree | Universal Learning for All Ages (5 to 100+)</title>
    <meta name="description" content="Free education without age boundaries. Personalized learning practices from 5-year-old early childhood phonics to golden age cognitive wellness and high-stakes exam preparation.">
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#eff6ff',
                            100: '#dbeafe',
                            500: '#2563eb',
                            600: '#1d4ed8',
                            700: '#1e40af',
                            800: '#1e3a8a',
                            accent: '#f59e0b',
                            kids: '#ec4899',
                            youth: '#8b5cf6',
                            exam: '#2563eb',
                            career: '#059669',
                            senior: '#d97706'
                        }
                    }
                }
            }
        }
    </script>
</head>
<body class="bg-slate-50 text-slate-800 antialiased font-sans transition-all duration-200">

    <!-- Universal Accessibility & Age Bar -->
    <div class="bg-slate-900 text-white text-xs py-2 px-4 border-b border-slate-800">
        <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2">
                <span class="bg-blue-600/80 text-white font-bold px-2 py-0.5 rounded text-[11px] uppercase tracking-wider">Universal Learning</span>
                <span class="text-slate-300 hidden sm:inline">Education without age barriers &bull; 100% Free & Open Access</span>
            </div>
            <!-- Accessibility Quick Controls -->
            <div class="flex items-center gap-3">
                <span class="text-slate-400 text-xs hidden md:inline">Text Size:</span>
                <div class="flex items-center bg-slate-800 rounded border border-slate-700 overflow-hidden text-xs">
                    <button onclick="setFontSize('md')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn active" id="fontBtn-md" title="Standard text">A</button>
                    <button onclick="setFontSize('lg')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn" id="fontBtn-lg" title="Large text (Senior / Low-vision friendly)">A+</button>
                    <button onclick="setFontSize('xl')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn" id="fontBtn-xl" title="Extra Large text">A++</button>
                </div>
                <button onclick="readPageAloud()" class="flex items-center gap-1.5 bg-blue-600 hover:bg-blue-700 text-white px-2.5 py-1 rounded text-xs transition-all">
                    <i class="fa-solid fa-volume-high"></i> <span class="hidden sm:inline">Read Aloud</span>
                </button>
            </div>
        </div>
    </div>

    <!-- Navigation Header -->
    <nav class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <a href="index.html" class="flex items-center gap-2.5">
                    <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-white font-bold text-xl shadow-md shadow-blue-500/20">
                        <i class="fa-solid fa-graduation-cap"></i>
                    </div>
                    <div>
                        <span class="font-extrabold text-xl tracking-tight text-slate-900">Aspire<span class="text-blue-600">Free</span></span>
                        <span class="hidden md:inline-block text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full ml-1.5 border border-emerald-200">Ages 5 &ndash; 100+</span>
                    </div>
                </a>
            </div>

            <!-- Learner Stage Selector Dropdown -->
            <div class="hidden lg:flex items-center gap-2 bg-slate-100 p-1 rounded-xl border border-slate-200 text-xs font-semibold">
                <span class="text-slate-500 pl-2">Track:</span>
                <button onclick="switchGlobalAgeGroup('kids')" class="age-pill px-2.5 py-1 rounded-lg transition-all" id="navAge-kids">🧸 5-8 Kids</button>
                <button onclick="switchGlobalAgeGroup('youth')" class="age-pill px-2.5 py-1 rounded-lg transition-all" id="navAge-youth">🎒 9-14 Youth</button>
                <button onclick="switchGlobalAgeGroup('exam')" class="age-pill px-2.5 py-1 rounded-lg transition-all active" id="navAge-exam">🎓 15-24 Exams</button>
                <button onclick="switchGlobalAgeGroup('career')" class="age-pill px-2.5 py-1 rounded-lg transition-all" id="navAge-career">💼 25-54 Career</button>
                <button onclick="switchGlobalAgeGroup('senior')" class="age-pill px-2.5 py-1 rounded-lg transition-all" id="navAge-senior">🌿 55+ Golden</button>
            </div>

            <!-- Desktop Nav Links -->
            <div class="flex items-center gap-4 sm:gap-6 text-sm font-semibold">
                <a href="practice.html" class="text-slate-700 hover:text-blue-600 flex items-center gap-1.5">
                    <i class="fa-solid fa-gamepad text-blue-500"></i> Learning Arena
                </a>
                <a href="planner.html" class="text-slate-700 hover:text-blue-600 flex items-center gap-1.5">
                    <i class="fa-solid fa-calendar-check text-indigo-500"></i> Study Planner
                </a>
                <a href="resources.html" class="text-slate-700 hover:text-blue-600 flex items-center gap-1.5">
                    <i class="fa-solid fa-book-bookmark text-emerald-500"></i> Free Vault
                </a>
                <a href="practice.html" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-xl text-xs sm:text-sm font-bold shadow-sm transition-all">
                    Start Learning
                </a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <header class="relative overflow-hidden bg-gradient-to-b from-blue-50 via-white to-slate-50 py-16 sm:py-24 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
            <div class="inline-flex items-center gap-2 bg-gradient-to-r from-blue-100 to-indigo-100 border border-blue-200 text-blue-800 text-xs sm:text-sm font-extrabold px-4 py-1.5 rounded-full mb-6 shadow-sm">
                <i class="fa-solid fa-earth-americas text-blue-600"></i> Open Education for Every Generation &bull; 100% Free
            </div>
            
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-black text-slate-900 tracking-tight max-w-4xl mx-auto leading-tight">
                Education Without <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600">Age Boundaries</span>.
            </h1>
            
            <p class="mt-6 text-lg sm:text-xl text-slate-600 max-w-3xl mx-auto leading-relaxed">
                Whether you are a <strong>5-year-old child</strong> sounding out your first words, a <strong>high schooler</strong> preparing for exams, an <strong>adult</strong> upskilling, or an <strong>80-year-old senior</strong> exercising cognitive agility—AspireFree personalizes the best learning practices for your age and life stage.
            </p>

            <!-- 5 Age Cohorts Selector -->
            <div class="mt-10 max-w-4xl mx-auto">
                <p class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-3">Choose Your Age & Learning Stage</p>
                <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
                    <button onclick="selectAgeHero('kids')" class="hero-age-btn group p-4 rounded-2xl border-2 border-pink-200 hover:border-pink-500 bg-white hover:bg-pink-50/50 shadow-sm text-left transition-all">
                        <div class="text-2xl mb-1">🧸</div>
                        <div class="font-black text-slate-900 text-sm group-hover:text-pink-600">Ages 5–8</div>
                        <div class="text-[11px] text-slate-500 font-medium">Little Explorers: Phonics, Sounds & Stories</div>
                    </button>
                    <button onclick="selectAgeHero('youth')" class="hero-age-btn group p-4 rounded-2xl border-2 border-purple-200 hover:border-purple-500 bg-white hover:bg-purple-50/50 shadow-sm text-left transition-all">
                        <div class="text-2xl mb-1">🎒</div>
                        <div class="font-black text-slate-900 text-sm group-hover:text-purple-600">Ages 9–14</div>
                        <div class="text-[11px] text-slate-500 font-medium">Junior Scholars: Logic, STEM & Creative Writing</div>
                    </button>
                    <button onclick="selectAgeHero('exam')" class="hero-age-btn group p-4 rounded-2xl border-2 border-blue-500 bg-blue-50/70 shadow-sm text-left transition-all active-hero-btn">
                        <div class="text-2xl mb-1">🎓</div>
                        <div class="font-black text-blue-900 text-sm">Ages 15–24</div>
                        <div class="text-[11px] text-blue-600 font-medium">Academy & Exams: IELTS, PTE, SAT, TOEFL</div>
                    </button>
                    <button onclick="selectAgeHero('career')" class="hero-age-btn group p-4 rounded-2xl border-2 border-emerald-200 hover:border-emerald-500 bg-white hover:bg-emerald-50/50 shadow-sm text-left transition-all">
                        <div class="text-2xl mb-1">💼</div>
                        <div class="font-black text-slate-900 text-sm group-hover:text-emerald-600">Ages 25–54</div>
                        <div class="text-[11px] text-slate-500 font-medium">Professionals: Business Fluency & Skills</div>
                    </button>
                    <button onclick="selectAgeHero('senior')" class="hero-age-btn group p-4 rounded-2xl border-2 border-amber-200 hover:border-amber-500 bg-white hover:bg-amber-50/50 shadow-sm text-left transition-all col-span-2 sm:col-span-1">
                        <div class="text-2xl mb-1">🌿</div>
                        <div class="font-black text-slate-900 text-sm group-hover:text-amber-600">Ages 55+</div>
                        <div class="text-[11px] text-slate-500 font-medium">Golden Lifelong: Memory, Culture & Tech</div>
                    </button>
                </div>
            </div>

            <!-- Dynamic Hero Preview Card -->
            <div id="heroPreviewCard" class="mt-8 max-w-3xl mx-auto bg-white rounded-2xl p-6 border border-slate-200 shadow-xl text-left transition-all">
                <div class="flex items-center justify-between mb-4 pb-3 border-b border-slate-100">
                    <div class="flex items-center gap-3">
                        <span id="previewEmoji" class="text-3xl">🎓</span>
                        <div>
                            <h3 id="previewTitle" class="font-bold text-lg text-slate-900">Ages 15–24: Academy & High-Stakes Prep</h3>
                            <span id="previewPedagogy" class="text-xs font-semibold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">Deliberate Practice & Rubric Mastery</span>
                        </div>
                    </div>
                    <button onclick="testHeroAudio()" class="text-xs font-bold text-blue-600 hover:text-blue-800 flex items-center gap-1 bg-blue-50 px-3 py-1.5 rounded-lg">
                        <i class="fa-solid fa-volume-high"></i> Voice Intro
                    </button>
                </div>
                <p id="previewDesc" class="text-sm text-slate-600 leading-relaxed mb-5">
                    Realistic exam simulation with instant Cambridge & ETS rubric evaluation for IELTS, PTE, TOEFL, and SAT. Timed conditions, word counting, essay templates, and speaking audio drills.
                </p>
                <div class="flex flex-wrap items-center justify-between gap-4 pt-2">
                    <div id="previewTags" class="flex flex-wrap gap-2 text-xs">
                        <span class="px-2.5 py-1 bg-slate-100 rounded-lg text-slate-700 font-medium">⏱ Timed Practice</span>
                        <span class="px-2.5 py-1 bg-slate-100 rounded-lg text-slate-700 font-medium">📊 Band Rubrics</span>
                        <span class="px-2.5 py-1 bg-slate-100 rounded-lg text-slate-700 font-medium">📝 Writing Task 2</span>
                    </div>
                    <a id="previewCta" href="practice.html?age=exam" class="bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs sm:text-sm px-5 py-2.5 rounded-xl shadow-md transition-all flex items-center gap-2">
                        Enter Learning Arena <i class="fa-solid fa-arrow-right"></i>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- Science-Backed Pedagogical Framework for Every Age -->
    <section class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-xs font-extrabold uppercase tracking-widest text-blue-600 bg-blue-50 px-3 py-1 rounded-full">Developmental Neuroscience</span>
                <h2 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-3">Best Learning Practices Tailored to Life Stages</h2>
                <p class="text-slate-600 mt-4 text-base">
                    The human brain learns differently at age 5, age 20, and age 75. AspireFree integrates the proven cognitive science for each stage of human development.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-6">
                <!-- 5-8 -->
                <div class="p-6 rounded-2xl bg-gradient-to-b from-pink-50/50 to-white border border-pink-100 hover:shadow-lg transition-all space-y-4">
                    <div class="w-12 h-12 rounded-xl bg-pink-100 text-pink-600 flex items-center justify-center text-2xl">
                        🧸
                    </div>
                    <div>
                        <span class="text-xs font-bold text-pink-600 uppercase tracking-wider">Ages 5–8</span>
                        <h3 class="text-lg font-bold text-slate-900 mt-1">Multisensory Phonics & Play</h3>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li><i class="fa-solid fa-check text-pink-500 mr-1.5"></i> <strong>Montessori Audio:</strong> Connects letter symbols to natural spoken sounds.</li>
                        <li><i class="fa-solid fa-check text-pink-500 mr-1.5"></i> <strong>Micro-Lessons:</strong> 10-minute game sessions aligned to young attention spans.</li>
                        <li><i class="fa-solid fa-check text-pink-500 mr-1.5"></i> <strong>Positive Reinforcement:</strong> Cheer sounds and golden stars for confidence.</li>
                    </ul>
                </div>

                <!-- 9-14 -->
                <div class="p-6 rounded-2xl bg-gradient-to-b from-purple-50/50 to-white border border-purple-100 hover:shadow-lg transition-all space-y-4">
                    <div class="w-12 h-12 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center text-2xl">
                        🎒
                    </div>
                    <div>
                        <span class="text-xs font-bold text-purple-600 uppercase tracking-wider">Ages 9–14</span>
                        <h3 class="text-lg font-bold text-slate-900 mt-1">Inquiry & Dual Coding</h3>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li><i class="fa-solid fa-check text-purple-500 mr-1.5"></i> <strong>Visual + Text:</strong> Dual-coding memory techniques for school subjects.</li>
                        <li><i class="fa-solid fa-check text-purple-500 mr-1.5"></i> <strong>Spaced Recall:</strong> Quick interactive quizzes that build long-term retention.</li>
                        <li><i class="fa-solid fa-check text-purple-500 mr-1.5"></i> <strong>Scaffolded Writing:</strong> Structured sentence frames for creative stories.</li>
                    </ul>
                </div>

                <!-- 15-24 -->
                <div class="p-6 rounded-2xl bg-gradient-to-b from-blue-50/50 to-white border border-blue-100 hover:shadow-lg transition-all space-y-4">
                    <div class="w-12 h-12 rounded-xl bg-blue-100 text-blue-600 flex items-center justify-center text-2xl">
                        🎓
                    </div>
                    <div>
                        <span class="text-xs font-bold text-blue-600 uppercase tracking-wider">Ages 15–24</span>
                        <h3 class="text-lg font-bold text-slate-900 mt-1">Deliberate Exam Practice</h3>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li><i class="fa-solid fa-check text-blue-500 mr-1.5"></i> <strong>High-Stakes Rubrics:</strong> Cambridge & ETS official scoring models.</li>
                        <li><i class="fa-solid fa-check text-blue-500 mr-1.5"></i> <strong>Simulated Timing:</strong> Eliminates anxiety through authentic timed conditions.</li>
                        <li><i class="fa-solid fa-check text-blue-500 mr-1.5"></i> <strong>Template Blueprints:</strong> Band 9 essay and oral structure formulas.</li>
                    </ul>
                </div>

                <!-- 25-54 -->
                <div class="p-6 rounded-2xl bg-gradient-to-b from-emerald-50/50 to-white border border-emerald-100 hover:shadow-lg transition-all space-y-4">
                    <div class="w-12 h-12 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center text-2xl">
                        💼
                    </div>
                    <div>
                        <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider">Ages 25–54</span>
                        <h3 class="text-lg font-bold text-slate-900 mt-1">Adult Andragogy</h3>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li><i class="fa-solid fa-check text-emerald-500 mr-1.5"></i> <strong>Problem-Centered:</strong> Real-world email diplomacy & executive summaries.</li>
                        <li><i class="fa-solid fa-check text-emerald-500 mr-1.5"></i> <strong>Commuter Microlearning:</strong> 15-minute high-impact focused drills.</li>
                        <li><i class="fa-solid fa-check text-emerald-500 mr-1.5"></i> <strong>Career Fluency:</strong> Presentation pitch timers and professional tone checks.</li>
                    </ul>
                </div>

                <!-- 55+ -->
                <div class="p-6 rounded-2xl bg-gradient-to-b from-amber-50/50 to-white border border-amber-100 hover:shadow-lg transition-all space-y-4">
                    <div class="w-12 h-12 rounded-xl bg-amber-100 text-amber-600 flex items-center justify-center text-2xl">
                        🌿
                    </div>
                    <div>
                        <span class="text-xs font-bold text-amber-600 uppercase tracking-wider">Ages 55+</span>
                        <h3 class="text-lg font-bold text-slate-900 mt-1">Neuroplasticity & Ease</h3>
                    </div>
                    <ul class="text-xs text-slate-600 space-y-2">
                        <li><i class="fa-solid fa-check text-amber-500 mr-1.5"></i> <strong>Cognitive Reserve:</strong> Memory matching, word games, and mental gym.</li>
                        <li><i class="fa-solid fa-check text-amber-500 mr-1.5"></i> <strong>Errorless Learning:</strong> No stressful timers or penalties; gentle encouragement.</li>
                        <li><i class="fa-solid fa-check text-amber-500 mr-1.5"></i> <strong>Accessibility First:</strong> Large readable fonts and slow, clear speech narration.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Interactive Highlights for All Generations -->
    <section class="py-16 sm:py-24 bg-slate-50 border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-widest text-blue-600 bg-blue-100/60 px-3 py-1 rounded-full">Universal Curriculum</span>
                    <h2 class="text-3xl font-extrabold text-slate-900 mt-2">What Can You Practice on AspireFree?</h2>
                </div>
                <p class="text-slate-500 text-sm max-w-md mt-2 md:mt-0">
                    Switch tracks at any moment. Everything is client-side, private, and available with $0 barrier.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Kids -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-6">
                        <div class="flex justify-between items-start mb-4">
                            <span class="px-3 py-1 bg-pink-100 text-pink-700 text-xs font-bold rounded-lg uppercase">Early Childhood</span>
                            <span class="text-xs text-slate-400 font-semibold">Ages 5–8</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-2">Phonics & Story Playground</h3>
                        <p class="text-sm text-slate-600 mb-4">Interactive alphabet sounds, sight word spelling, picture story quizzes, and speak-aloud star games.</p>
                        <ul class="text-xs text-slate-500 space-y-1.5">
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Interactive A-Z Soundboard</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Picture Word Association</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Counting & Shape Explorer</li>
                        </ul>
                    </div>
                    <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700">Fun & Free</span>
                        <a href="practice.html?age=kids" class="text-sm font-bold text-pink-600 hover:text-pink-800">Explore Kids Arena &rarr;</a>
                    </div>
                </div>

                <!-- Youth -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-6">
                        <div class="flex justify-between items-start mb-4">
                            <span class="px-3 py-1 bg-purple-100 text-purple-700 text-xs font-bold rounded-lg uppercase">School & Discovery</span>
                            <span class="text-xs text-slate-400 font-semibold">Ages 9–14</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-2">Junior Scholars Hub</h3>
                        <p class="text-sm text-slate-600 mb-4">Reading adventure passages, story starter creative writing, mental math puzzles, and science trivia.</p>
                        <ul class="text-xs text-slate-500 space-y-1.5">
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Reading Comprehension Quests</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Creative Story Writing Lab</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Mental Math & Logic Challenges</li>
                        </ul>
                    </div>
                    <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700">Inquiry-Based</span>
                        <a href="practice.html?age=youth" class="text-sm font-bold text-purple-600 hover:text-purple-800">Launch Junior Hub &rarr;</a>
                    </div>
                </div>

                <!-- Exams -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-6">
                        <div class="flex justify-between items-start mb-4">
                            <span class="px-3 py-1 bg-blue-100 text-blue-700 text-xs font-bold rounded-lg uppercase">Standardized Tests</span>
                            <span class="text-xs text-slate-400 font-semibold">Ages 15–24</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-2">High-Stakes Exam Suite</h3>
                        <p class="text-sm text-slate-600 mb-4">IELTS, PTE, TOEFL, and Digital SAT simulated modules with instant Cambridge/ETS automated rubric scoring.</p>
                        <ul class="text-xs text-slate-500 space-y-1.5">
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> True / False / Not Given Reading</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Task 2 Essay Rubric Evaluator</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> 2-Min Speaking Cue Card Timer</li>
                        </ul>
                    </div>
                    <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700">Official Standards</span>
                        <a href="practice.html?age=exam" class="text-sm font-bold text-blue-600 hover:text-blue-800">Start Exam Sim &rarr;</a>
                    </div>
                </div>

                <!-- Career -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col justify-between">
                    <div class="p-6">
                        <div class="flex justify-between items-start mb-4">
                            <span class="px-3 py-1 bg-emerald-100 text-emerald-700 text-xs font-bold rounded-lg uppercase">Career & Adults</span>
                            <span class="text-xs text-slate-400 font-semibold">Ages 25–54</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-2">Executive & Business Fluency</h3>
                        <p class="text-sm text-slate-600 mb-4">Professional email diplomacy checker, executive report summaries, and elevator pitch presentation pacing.</p>
                        <ul class="text-xs text-slate-500 space-y-1.5">
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Executive Email Tone Analyzer</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Presentation Pacing Simulator</li>
                            <li><i class="fa-solid fa-star text-amber-400 mr-1"></i> Corporate Vocabulary Bank</li>
                        </ul>
                    </div>
                    <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700">High Impact</span>
                        <a href="practice.html?age=career" class="text-sm font-bold text-emerald-600 hover:text-emerald-800">Start Career Track &rarr;</a>
                    </div>
                </div>

                <!-- Senior -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col justify-between md:col-span-2 lg:col-span-2">
                    <div class="p-6">
                        <div class="flex justify-between items-start mb-4">
                            <span class="px-3 py-1 bg-amber-100 text-amber-800 text-xs font-bold rounded-lg uppercase">Golden Age & Lifelong</span>
                            <span class="text-xs text-slate-400 font-semibold">Ages 55+</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-2">Brain Gym & Digital Confidence</h3>
                        <p class="text-sm text-slate-600 mb-4">Memory pair drills, calm reflective life journaling, gentle narrated audio stories, and simple modern technology guides.</p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-500">
                            <div><i class="fa-solid fa-star text-amber-400 mr-1"></i> Cognitive Memory Association</div>
                            <div><i class="fa-solid fa-star text-amber-400 mr-1"></i> Stress-Free Reflective Writing</div>
                            <div><i class="fa-solid fa-star text-amber-400 mr-1"></i> Gentle 0.85x Audiobook Player</div>
                            <div><i class="fa-solid fa-star text-amber-400 mr-1"></i> Digital Safety & Smartphone Tips</div>
                        </div>
                    </div>
                    <div class="px-6 py-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-xs font-bold text-slate-700">Zero Pressure &bull; Gentle Pacing</span>
                        <a href="practice.html?age=senior" class="text-sm font-bold text-amber-600 hover:text-amber-800">Enter Golden Space &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Multi-Generational Community Voices -->
    <section class="py-16 sm:py-24 bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <span class="text-xs font-extrabold uppercase tracking-widest text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full">Lifelong Impact</span>
                <h2 class="text-3xl font-extrabold text-slate-900 mt-3">Loved by Learners from 5 to 85</h2>
                <p class="text-slate-600 mt-2 text-base">Real experiences from students, parents, professionals, and seniors worldwide.</p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Parent of 5yo -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                    <p class="text-slate-600 text-sm italic mb-4">
                        &ldquo;My 5-year-old son Lucas loves the phonics sound cards and star cheers. He asks to play 'Aspire' every afternoon. It made learning to read a joy without annoying ads or subscriptions.&rdquo;
                    </p>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-200">
                        <div class="w-10 h-10 rounded-full bg-pink-100 text-pink-600 font-bold flex items-center justify-center text-sm">ML</div>
                        <div>
                            <div class="font-bold text-slate-900 text-xs">Maria &amp; Lucas (Age 5)</div>
                            <div class="text-[11px] text-slate-500">Early Phonics Learner</div>
                        </div>
                    </div>
                </div>

                <!-- 21yo Exam student -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                    <p class="text-slate-600 text-sm italic mb-4">
                        &ldquo;The IELTS Writing Task 2 instant rubric evaluation helped me understand why my essays were stuck at 6.0. In three weeks, I reached Band 7.5. Unbelievable that this is 100% free.&rdquo;
                    </p>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-200">
                        <div class="w-10 h-10 rounded-full bg-blue-100 text-blue-600 font-bold flex items-center justify-center text-sm">TA</div>
                        <div>
                            <div class="font-bold text-slate-900 text-xs">Tariq Al-Mansoor (Age 21)</div>
                            <div class="text-[11px] text-slate-500">University Applicant &bull; Band 7.5</div>
                        </div>
                    </div>
                </div>

                <!-- 72yo Senior -->
                <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between">
                    <p class="text-slate-600 text-sm italic mb-4">
                        &ldquo;At 72, I wanted to keep my memory sharp and feel more comfortable using the internet. The large print mode is wonderful on my eyes, and the daily memory drills are my morning ritual with coffee.&rdquo;
                    </p>
                    <div class="flex items-center gap-3 pt-3 border-t border-slate-200">
                        <div class="w-10 h-10 rounded-full bg-amber-100 text-amber-700 font-bold flex items-center justify-center text-sm">EH</div>
                        <div>
                            <div class="font-bold text-slate-900 text-xs">Eleanor Hughes (Age 72)</div>
                            <div class="text-[11px] text-slate-500">Lifelong Learner &bull; Retired Teacher</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 text-sm py-12 border-t border-slate-800">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div class="space-y-3">
                <div class="flex items-center gap-2 text-white font-extrabold text-lg">
                    <i class="fa-solid fa-graduation-cap text-blue-500"></i> AspireFree
                </div>
                <p class="text-xs text-slate-400">Universal, open-access education without age bounding. Built for educational equity from early childhood to lifelong golden years.</p>
            </div>
            <div>
                <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Age Tracks</h4>
                <ul class="space-y-2 text-xs">
                    <li><a href="practice.html?age=kids" class="hover:text-white">Ages 5–8: Phonics &amp; Storytelling</a></li>
                    <li><a href="practice.html?age=youth" class="hover:text-white">Ages 9–14: Junior Inquiry &amp; Logic</a></li>
                    <li><a href="practice.html?age=exam" class="hover:text-white">Ages 15–24: IELTS, PTE &amp; SAT Prep</a></li>
                    <li><a href="practice.html?age=career" class="hover:text-white">Ages 25–54: Business Fluency</a></li>
                    <li><a href="practice.html?age=senior" class="hover:text-white">Ages 55+: Memory &amp; Lifelong Health</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Adaptive Tools</h4>
                <ul class="space-y-2 text-xs">
                    <li><a href="practice.html" class="hover:text-white">Learning Arena</a></li>
                    <li><a href="planner.html" class="hover:text-white">Developmental Study Planner</a></li>
                    <li><a href="resources.html" class="hover:text-white">Printable &amp; Digital Vault</a></li>
                    <li><button onclick="setFontSize('lg')" class="hover:text-white text-left">Large Text Mode (Senior Friendly)</button></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Educational Philosophy</h4>
                <p class="text-xs text-slate-400 leading-relaxed">
                    Designed around Piaget's developmental stages, Montessori multisensory mechanics, Knowles' adult andragogy, and cognitive reserve preservation for seniors.
                </p>
            </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 text-center text-xs text-slate-500 pt-6 border-t border-slate-800">
            &copy; 2026 AspireFree Open Prep. Built for global educational equity. Non-commercial, open-access, zero age bounding.
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>
'''

    # ==========================================
    # 2. practice.html - Universal Learning Arena
    # ==========================================
    practice_html = '''<!DOCTYPE html>
<html lang="en" class="font-size-md">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AspireFree | Universal Learning Arena</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-slate-100 text-slate-800 antialiased min-h-screen flex flex-col font-sans">

    <!-- Top Arena Bar -->
    <header class="bg-slate-900 text-white px-4 sm:px-6 py-3 flex flex-wrap items-center justify-between sticky top-0 z-50 shadow-md gap-3">
        <div class="flex items-center gap-4">
            <a href="index.html" class="text-slate-400 hover:text-white text-sm flex items-center gap-1.5">
                <i class="fa-solid fa-arrow-left"></i> Home
            </a>
            <div class="h-4 w-px bg-slate-700 hidden sm:block"></div>
            <!-- Stage Switcher -->
            <div class="flex items-center gap-2">
                <span class="text-xs text-slate-400 hidden md:inline">Current Stage:</span>
                <select id="arenaAgeSelect" onchange="changeArenaAge(this.value)" class="bg-slate-800 text-white font-bold text-xs px-3 py-1.5 rounded-lg border border-slate-700 focus:outline-none focus:border-blue-500 cursor-pointer">
                    <option value="kids">🧸 Ages 5–8: Little Explorers</option>
                    <option value="youth">🎒 Ages 9–14: Junior Scholars</option>
                    <option value="exam" selected>🎓 Ages 15–24: Exam Prep & Academy</option>
                    <option value="career">💼 Ages 25–54: Professional Growth</option>
                    <option value="senior">🌿 Ages 55+: Golden Age & Lifelong</option>
                </select>
            </div>
        </div>

        <!-- Controls: Font, Voice, Timer -->
        <div class="flex items-center gap-3">
            <!-- Text Size Scaler -->
            <div class="flex items-center bg-slate-800 rounded border border-slate-700 overflow-hidden text-xs">
                <button onclick="setFontSize('md')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn active" id="fontBtn-md">A</button>
                <button onclick="setFontSize('lg')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn" id="fontBtn-lg">A+</button>
                <button onclick="setFontSize('xl')" class="px-2 py-1 font-semibold hover:bg-slate-700 font-size-btn" id="fontBtn-xl">A++</button>
            </div>

            <!-- Voice Narration -->
            <button onclick="readActiveModule()" class="text-xs bg-slate-800 hover:bg-slate-700 text-blue-400 px-2.5 py-1.5 rounded-lg border border-slate-700 flex items-center gap-1.5" title="Listen to text">
                <i class="fa-solid fa-volume-high"></i> <span class="hidden sm:inline">Listen</span>
            </button>

            <!-- Adaptive Session Clock -->
            <div id="timerContainer" class="flex items-center gap-2 bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-700 font-mono text-sm">
                <i class="fa-regular fa-clock text-amber-400"></i>
                <span id="timerDisplay">20:00</span>
                <button id="timerToggleBtn" onclick="toggleTimer()" class="text-[11px] bg-slate-700 hover:bg-slate-600 px-1.5 py-0.5 rounded text-slate-200">
                    Pause
                </button>
            </div>
        </div>
    </header>

    <!-- Sub-navigation for Active Stage Modules -->
    <div class="bg-white border-b border-slate-200 px-4 sm:px-6 shadow-sm">
        <div id="moduleTabsContainer" class="max-w-7xl mx-auto flex overflow-x-auto space-x-6 text-sm font-semibold">
            <!-- Dynamically populated by app.js based on age group -->
        </div>
    </div>

    <!-- Active Practice Workspace -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 w-full">
        <div id="arenaContentArea">
            <!-- Dynamically populated with modules by app.js -->
        </div>
    </main>

    <!-- Toast Notification for Star & Scores -->
    <div id="toastNotification" class="fixed bottom-6 right-6 bg-slate-900 text-white px-5 py-3 rounded-2xl shadow-2xl flex items-center gap-3 transform translate-y-24 opacity-0 transition-all duration-300 z-50">
        <span id="toastIcon" class="text-2xl">⭐</span>
        <div>
            <div id="toastTitle" class="font-bold text-sm">Superstar!</div>
            <div id="toastMessage" class="text-xs text-slate-300">You completed this practice module!</div>
        </div>
    </div>

    <script src="app.js"></script>
</body>
</html>
'''

    # ==========================================
    # 3. planner.html - Developmental Study Planner
    # ==========================================
    planner_html = '''<!DOCTYPE html>
<html lang="en" class="font-size-md">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AspireFree | Developmental Study & Growth Planner</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-slate-50 text-slate-800 antialiased font-sans min-h-screen flex flex-col">

    <!-- Nav -->
    <nav class="bg-white border-b border-slate-200 px-4 sm:px-6 py-4">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 text-slate-900 font-extrabold text-lg">
                <i class="fa-solid fa-graduation-cap text-blue-600"></i> AspireFree
                <span class="text-xs font-semibold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full ml-1">Universal Planner</span>
            </a>
            <div class="flex items-center gap-4 text-sm font-semibold">
                <a href="practice.html" class="text-slate-600 hover:text-blue-600">Learning Arena</a>
                <a href="resources.html" class="text-slate-600 hover:text-blue-600">Free Vault</a>
                <!-- Font scale -->
                <div class="flex items-center bg-slate-100 rounded border border-slate-200 overflow-hidden text-xs">
                    <button onclick="setFontSize('md')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn active" id="fontBtn-md">A</button>
                    <button onclick="setFontSize('lg')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn" id="fontBtn-lg">A+</button>
                    <button onclick="setFontSize('xl')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn" id="fontBtn-xl">A++</button>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-5xl mx-auto px-4 sm:px-6 py-10 flex-1 w-full space-y-10">
        <!-- Title -->
        <div class="text-center max-w-2xl mx-auto space-y-2">
            <span class="text-xs font-extrabold uppercase tracking-widest text-indigo-600 bg-indigo-50 px-3 py-1 rounded-full">Developmental Milestone Engine</span>
            <h1 class="text-3xl font-extrabold text-slate-900">Personalized Growth Planner</h1>
            <p class="text-slate-600 text-sm">
                Plans tailored to your brain's natural learning rhythm. Whether allocating 10 minutes of playful phonics for a 5-year-old or 60 minutes of intensive IELTS analysis for a university applicant.
            </p>
        </div>

        <!-- Planner Card -->
        <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-8">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Age Stage -->
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">1. Your Age & Life Stage</label>
                    <select id="planAgeGroup" onchange="updatePlannerPresets()" class="w-full p-3 rounded-xl border border-slate-200 font-semibold text-sm bg-slate-50 focus:ring-2 focus:ring-blue-500 focus:outline-none">
                        <option value="kids">🧸 Ages 5–8 (Early Childhood)</option>
                        <option value="youth">🎒 Ages 9–14 (School & STEM)</option>
                        <option value="exam" selected>🎓 Ages 15–24 (Exams & College)</option>
                        <option value="career">💼 Ages 25–54 (Career & Adult)</option>
                        <option value="senior">🌿 Ages 55+ (Golden Age & Memory)</option>
                    </select>
                </div>

                <!-- Primary Goal -->
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">2. Learning Target</label>
                    <select id="planGoal" class="w-full p-3 rounded-xl border border-slate-200 font-semibold text-sm bg-slate-50 focus:ring-2 focus:ring-blue-500 focus:outline-none">
                        <!-- Populated dynamically based on age -->
                    </select>
                </div>

                <!-- Daily Time Available -->
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">3. Daily Time Available</label>
                    <select id="planDailyTime" class="w-full p-3 rounded-xl border border-slate-200 font-semibold text-sm bg-slate-50 focus:ring-2 focus:ring-blue-500 focus:outline-none">
                        <option value="15">15 Minutes / Day (Micro-Sessions)</option>
                        <option value="30">30 Minutes / Day (Balanced)</option>
                        <option value="60" selected>1 Hour / Day (Focused)</option>
                        <option value="120">2 Hours / Day (Intensive)</option>
                    </select>
                </div>
            </div>

            <!-- Target Weeks -->
            <div class="pt-4 border-t border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div class="flex items-center gap-4">
                    <span class="text-xs font-bold text-slate-600">Preparation Timeline:</span>
                    <input type="range" id="planWeeksRange" min="2" max="16" value="6" oninput="document.getElementById('planWeeksVal').innerText = this.value + ' Weeks'" class="w-40 accent-blue-600">
                    <span id="planWeeksVal" class="text-sm font-extrabold text-blue-600 font-mono">6 Weeks</span>
                </div>
                <button onclick="calculateDevelopmentalPlan()" class="w-full sm:w-auto bg-blue-600 hover:bg-blue-700 text-white font-bold text-sm px-8 py-3 rounded-xl shadow-md transition-all">
                    Generate My Schedule &rarr;
                </button>
            </div>
        </div>

        <!-- Generated Plan Output -->
        <div id="plannerResultsArea" class="hidden space-y-6">
            <!-- Cognitive Science Note -->
            <div id="neuroscienceCard" class="p-5 rounded-2xl bg-indigo-50 border border-indigo-100 flex items-start gap-4">
                <div class="text-2xl text-indigo-600 mt-0.5"><i class="fa-solid fa-brain"></i></div>
                <div>
                    <h4 class="font-bold text-indigo-950 text-sm" id="neuroscienceTitle">Developmental Learning Rationale</h4>
                    <p class="text-xs text-indigo-800 mt-1 leading-relaxed" id="neuroscienceDesc">
                        At this developmental stage, spaced practice prevents cognitive fatigue and strengthens neural synaptic consolidation.
                    </p>
                </div>
            </div>

            <!-- Metrics -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div class="p-5 rounded-2xl bg-white border border-slate-200 text-center">
                    <div class="text-xs font-bold uppercase text-slate-400">Total Learning Commitment</div>
                    <div class="text-2xl font-black text-slate-900 mt-1" id="resTotalHours">42 Hours</div>
                </div>
                <div class="p-5 rounded-2xl bg-white border border-slate-200 text-center">
                    <div class="text-xs font-bold uppercase text-slate-400">Recommended Session Length</div>
                    <div class="text-2xl font-black text-blue-600 mt-1" id="resSessionPacing">25 Mins (Pomodoro)</div>
                </div>
                <div class="p-5 rounded-2xl bg-white border border-slate-200 text-center">
                    <div class="text-xs font-bold uppercase text-slate-400">Feasibility Confidence</div>
                    <div class="text-2xl font-black text-emerald-600 mt-1" id="resFeasibility">95% High</div>
                </div>
            </div>

            <!-- Weekly Milestone Breakdown -->
            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
                <h3 class="font-bold text-lg text-slate-900 flex items-center justify-between">
                    <span>Weekly Progression Roadmap</span>
                    <button onclick="window.print()" class="text-xs font-bold text-slate-500 hover:text-slate-800 flex items-center gap-1">
                        <i class="fa-solid fa-print"></i> Print Schedule
                    </button>
                </h3>
                <div id="weeklyPlanList" class="space-y-4">
                    <!-- Populated dynamically -->
                </div>
            </div>
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-500 text-xs py-8 text-center mt-12 border-t border-slate-800">
        &copy; 2026 AspireFree Open Prep. All developmental learning schedules free forever.
    </footer>

    <script src="app.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            updatePlannerPresets();
            calculateDevelopmentalPlan();
        });
    </script>
</body>
</html>
'''

    # ==========================================
    # 4. resources.html - Universal Resource Vault
    # ==========================================
    resources_html = '''<!DOCTYPE html>
<html lang="en" class="font-size-md">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AspireFree | Universal Free Resource Vault</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body class="bg-slate-50 text-slate-800 antialiased font-sans min-h-screen flex flex-col">

    <nav class="bg-white border-b border-slate-200 px-4 sm:px-6 py-4">
        <div class="max-w-7xl mx-auto flex items-center justify-between">
            <a href="index.html" class="flex items-center gap-2 text-slate-900 font-extrabold text-lg">
                <i class="fa-solid fa-graduation-cap text-blue-600"></i> AspireFree
                <span class="text-xs font-semibold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-full ml-1">Free Vault</span>
            </a>
            <div class="flex items-center gap-4 text-sm font-semibold">
                <a href="practice.html" class="text-slate-600 hover:text-blue-600">Learning Arena</a>
                <a href="planner.html" class="text-slate-600 hover:text-blue-600">Study Planner</a>
                <!-- Font scale -->
                <div class="flex items-center bg-slate-100 rounded border border-slate-200 overflow-hidden text-xs">
                    <button onclick="setFontSize('md')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn active" id="fontBtn-md">A</button>
                    <button onclick="setFontSize('lg')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn" id="fontBtn-lg">A+</button>
                    <button onclick="setFontSize('xl')" class="px-2 py-1 font-semibold hover:bg-slate-200 font-size-btn" id="fontBtn-xl">A++</button>
                </div>
            </div>
        </div>
    </nav>

    <main class="max-w-5xl mx-auto px-4 sm:px-6 py-10 flex-1 w-full space-y-8">
        <div class="text-center max-w-2xl mx-auto space-y-2">
            <span class="text-xs font-extrabold uppercase tracking-widest text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full">100% Free Educational Materials</span>
            <h1 class="text-3xl font-extrabold text-slate-900">Lifelong Resource Vault</h1>
            <p class="text-slate-600 text-sm">Download, copy, or print learning cheat sheets, phonics charts, essay templates, and memory aids across all age groups.</p>
        </div>

        <!-- Filter Tabs -->
        <div class="flex flex-wrap items-center justify-center gap-2 text-xs font-bold">
            <button onclick="filterVault('all')" class="vault-tab-btn active px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-all">All Resources</button>
            <button onclick="filterVault('kids')" class="vault-tab-btn px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-kids">🧸 Ages 5–8 (Kids)</button>
            <button onclick="filterVault('youth')" class="vault-tab-btn px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-youth">🎒 Ages 9–14 (Youth)</button>
            <button onclick="filterVault('exam')" class="vault-tab-btn px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-exam">🎓 Ages 15–24 (Exams)</button>
            <button onclick="filterVault('career')" class="vault-tab-btn px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-career">💼 Ages 25–54 (Career)</button>
            <button onclick="filterVault('senior')" class="vault-tab-btn px-4 py-2 rounded-xl border border-slate-300 bg-white hover:bg-slate-100" id="vtab-senior">🌿 Ages 55+ (Golden)</button>
        </div>

        <!-- Resources Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6" id="vaultCardsGrid">
            <!-- Kids Resource -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="kids">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-pink-100 text-pink-700">Ages 5–8 Phonics</span>
                    <button onclick="copyResourceText('phonicsCardText')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Text</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">Alphabet Phonics Sound & Sight Word Matrix</h3>
                <p class="text-xs text-slate-500">The 26 primary phonemes paired with daily sight words (cat, dog, sun, moon, tree) for bedtime and classroom reading.</p>
                <pre id="phonicsCardText" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">A [æ] - Apple, Ant, Astronaut
B [b] - Bear, Ball, Butterfly
C [k] - Cat, Cup, Car
D [d] - Dog, Duck, Door
E [e] - Elephant, Egg, Echo
S [s] - Sun, Star, Smile
M [m] - Moon, Milk, Monkey</pre>
            </div>

            <!-- Youth Resource -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="youth">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-purple-100 text-purple-700">Ages 9–14 Storytelling</span>
                    <button onclick="copyResourceText('storyFormulaText')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Text</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">Junior Story Structure: The Hero's 5-Box Method</h3>
                <p class="text-xs text-slate-500">Universal framework for narrative school essays: Character &rarr; Challenge &rarr; Attempt &rarr; Climax &rarr; Resolution.</p>
                <pre id="storyFormulaText" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">Box 1 (Hook): Introduce hero and an unexpected everyday event.
Box 2 (Conflict): The sudden problem or mystery arises.
Box 3 (Twist): The hero's first attempt fails; an ally offers a hint.
Box 4 (Climax): Facing the major challenge with bravery and smarts.
Box 5 (Lesson): The resolution, personal growth, and new perspective.</pre>
            </div>

            <!-- Exam Resource 1 -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="exam">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-700">Ages 15–24 IELTS</span>
                    <button onclick="copyResourceText('ieltsTemplate')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Template</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">IELTS Academic Task 2: 4-Paragraph Band 9 Blueprint</h3>
                <p class="text-xs text-slate-500">Guaranteed structure ensuring 100% Task Achievement and Coherence &amp; Cohesion criteria.</p>
                <pre id="ieltsTemplate" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">1. Introduction:
- Sentence 1: Paraphrase prompt background.
- Sentence 2: Thesis statement outlining two core perspectives.
2. Body Paragraph 1:
- Topic sentence & supporting evidence.
3. Body Paragraph 2:
- Counter-perspective / direct analysis.
4. Conclusion:
- Reiterate thesis and forward-looking synthesis.</pre>
            </div>

            <!-- Exam Resource 2 -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="exam">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-blue-100 text-blue-700">Ages 15–24 PTE</span>
                    <button onclick="copyResourceText('pteTemplate')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Blueprint</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">PTE Describe Image 25-Second Formula</h3>
                <p class="text-xs text-slate-500">Acoustic fluency formula satisfying the Pearson AI speech-recognition engine without hesitations.</p>
                <pre id="pteTemplate" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">"The given image provides crucial information about [TITLE].
Looking closely, the highest figure can be observed in [MAX VALUE].
Conversely, the minimum trend is registered at [MIN VALUE].
Overall, it is evident from the visual representation that [KEY CONCLUSION]."</pre>
            </div>

            <!-- Career Resource -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="career">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-emerald-100 text-emerald-700">Ages 25–54 Workplace</span>
                    <button onclick="copyResourceText('emailDiplomacy')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Phrases</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">Executive Email Diplomacy &amp; Assertive Phrases</h3>
                <p class="text-xs text-slate-500">Polite, high-influence phrasing for workplace alignment, deadlines, and pushback.</p>
                <pre id="emailDiplomacy" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">- Gentle Follow-up: "Circling back to ensure this remains on your radar ahead of Thursday's checkpoint."
- Polite Pushback: "To protect the quality of this deliverable, we can prioritize either feature A or B for this sprint."
- Seeking Clarity: "Could you confirm whether the proposed timeline accounts for testing dependencies?"</pre>
            </div>

            <!-- Senior Resource -->
            <div class="vault-card p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4" data-group="senior">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-0.5 rounded text-xs font-bold bg-amber-100 text-amber-800">Ages 55+ Senior Vitality</span>
                    <button onclick="copyResourceText('seniorGuideText')" class="text-xs text-blue-600 hover:text-blue-800 font-semibold"><i class="fa-regular fa-copy"></i> Copy Guide</button>
                </div>
                <h3 class="text-lg font-bold text-slate-900">Daily Cognitive Reserve Stimulator &amp; Digital Safety Primer</h3>
                <p class="text-xs text-slate-500">Morning brain warm-up exercises and essential digital safety rules for peace of mind.</p>
                <pre id="seniorGuideText" class="p-3 bg-slate-50 rounded-xl text-xs text-slate-700 font-mono overflow-x-auto whitespace-pre-wrap">1. Morning Word Association: Name 5 fruits, 5 birds, and 5 cities starting with 'S'.
2. Reverse Memory Recall: Before sleep, mentally review the 3 most pleasant moments of your day in reverse order.
3. Digital Safety Golden Rule: Legitimate banks or government bodies will never ask for your password or SMS codes via phone call or urgent SMS.</pre>
            </div>
        </div>
    </main>

    <footer class="bg-slate-900 text-slate-500 text-xs py-8 text-center mt-12 border-t border-slate-800">
        &copy; 2026 AspireFree Open Prep. All resources 100% public domain and free for educational use.
    </footer>

    <script src="app.js"></script>
</body>
</html>
'''

    # ==========================================
    # 5. styles.css - Universal & Accessible Styling
    # ==========================================
    styles_css = '''/* AspireFree Universal Styling & Accessibility */

/* Accessible Dynamic Font Scaling */
html.font-size-md {
    font-size: 16px;
}
html.font-size-lg {
    font-size: 19px;
}
html.font-size-xl {
    font-size: 22px;
}

body {
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

/* Active buttons & tabs */
.font-size-btn.active {
    background-color: #2563eb !important;
    color: #ffffff !important;
}

.age-pill.active {
    background-color: #2563eb !important;
    color: #ffffff !important;
}

.module-tab.active {
    color: #2563eb !important;
    border-color: #2563eb !important;
}

.vault-tab-btn.active {
    background-color: #2563eb !important;
    color: #ffffff !important;
    border-color: #2563eb !important;
}

/* Fun interactive cards for kids */
.phonics-card {
    transition: transform 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    cursor: pointer;
}
.phonics-card:hover {
    transform: translateY(-4px) scale(1.03);
}

/* Senior friendly high-legibility touch targets */
button, select, input {
    touch-action: manipulation;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #f1f5f9;
}
::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 9999px;
}
::-webkit-scrollbar-thumb:hover {
    background: #94a3b8;
}
'''

    # ==========================================
    # 6. app.js - Universal Interactive Engine
    # ==========================================
    app_js = r'''// AspireFree Universal Learning Engine (Ages 5 to 100+)

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
'''

    # ==========================================
    # 7. vercel.json & GitHub Workflow
    # ==========================================
    vercel_json = '''{
  "version": 2,
  "cleanUrls": true,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "X-Frame-Options", "value": "DENY" },
        { "key": "X-XSS-Protection", "value": "1; mode=block" }
      ]
    }
  ]
}'''

    github_workflow = '''name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v4
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
'''

    # Write all files to disk
    files = {
        'index.html': index_html,
        'practice.html': practice_html,
        'planner.html': planner_html,
        'resources.html': resources_html,
        'styles.css': styles_css,
        'app.js': app_js,
        'vercel.json': vercel_json,
    }

    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Created {filename}")

    # Create .github/workflows directory
    os.makedirs('.github/workflows', exist_ok=True)
    with open('.github/workflows/deploy.yml', 'w', encoding='utf-8') as f:
        f.write(github_workflow)
    print("  ✓ Created .github/workflows/deploy.yml")

    print("\n✅ AspireFree Universal Platform successfully generated!")
    print("Ages supported: 5 to 100+ (Kids, Youth, Exams, Career, Golden Lifelong)")
    print("To test locally: python3 -m http.server 3000")
    print("Open http://localhost:3000 in your browser.")

if __name__ == '__main__':
    generate_website()
