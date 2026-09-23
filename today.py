#!/usr/bin/env python3
# Profile renderer source. The checked-in SVGs are generated from the user's portrait-derived ASCII.
# Edit profile text here, then regenerate if desired.
from pathlib import Path

ASCII = r"""                                              
                 ;XH&@@@BGhX.                 
               5@@@@@@@@@@@@@H.               
              B@@@@@@@@@@@@@@@@h              
             2@@#h52235XrX2h&@@@X             
             A@Gri;:::::,:;rAG&@,             
             ,BhhMh2r;:iX253h2S#,             
            .2SMHS#G3AiAhG#SM5M5s:            
             2G3XXsrsArsrrsssXh2s             
              A#Ai;:s2iXs::is5Sr              
               5&3A2H&9B#M52G@H               
                9@@@&9GS##@@@@X               
                 &@@99#9&9@@@9                
                 A#&@B@@@@@&SM,               
             iXh9BH55hhMM5A3MH9G2i,           
     :r2MS9@@@@@@@@@@@&B9B&@@@@@@@@@9G3Ar:    
  rG@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@93; 
:S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"""
PROFILE = {
    "name": "turkoise@github",
    "os": "macOS",
    "location": "Bulgaria",
    "role": "Frontend Developer",
    "status": "Open to work",
    "languages": "JavaScript, TypeScript, C#, Swift",
    "frameworks": "React, Next.js, React Native, Vite",
    "frontend": "Tailwind CSS, HTML, CSS",
    "backend": "Node.js, Supabase, REST APIs",
    "tools": "Git, GitHub, Figma, VS Code",
}
print("Profile source is configured. SVG assets are committed in the repository.")
