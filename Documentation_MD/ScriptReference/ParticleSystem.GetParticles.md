[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [ParticleSystem](ParticleSystem.html).GetParticles

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

## Declaration

public int GetParticles(out Particle[] particles);

## Declaration

public int GetParticles(out Particle[] particles, int size);

## Declaration

public int GetParticles(out Particle[] particles, int size, int offset);

## Declaration

public int GetParticles(out NativeArray<Particle> particles);

## Declaration

public int GetParticles(out NativeArray<Particle> particles, int size);

## Declaration

public int GetParticles(out NativeArray<Particle> particles, int size, int
offset);

### Parameters

particles | Output particle buffer, containing the current particle state.  
---|---  
size | The number of elements that are read from the Particle System.  
offset | The offset into the active particle list, from which to copy the particles.  
  
### Returns

**int** The number of particles written to the input particle array (the
number of particles currently alive).

### Description

Gets the particles of this Particle System.

This method is allocation free as long the input "particles" array is
preallocated once (see example below). The method only gets the particles that
are currently alive in the Particle System when it is called, so it may only
get a small part of the particles array.  
  
Additional resources: [Particle](ParticleSystem.Particle.html),
[SetParticles](ParticleSystem.SetParticles.html).

    
    
    using UnityEngine;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ParticleFlow : [MonoBehaviour](MonoBehaviour.html)
    {
        [ParticleSystem](ParticleSystem.html) m_System;
        [ParticleSystem.Particle](ParticleSystem.Particle.html)[] m_Particles;
        public float m_Drift = 0.01f;  
      
        private void LateUpdate()
        {
            InitializeIfNeeded();  
      
            // GetParticles is allocation free because we reuse the m_Particles buffer between updates
            int numParticlesAlive = m_System.GetParticles(m_Particles);  
      
            // Change only the particles that are alive
            for (int i = 0; i < numParticlesAlive; i++)
            {
                m_Particles[i].velocity += [Vector3.up](Vector3-up.html) * m_Drift;
            }  
      
            // Apply the particle changes to the [Particle](ParticleSystem.Particle.html) [System](Rendering.VirtualTexturing.System.html)
            m_System.SetParticles(m_Particles, numParticlesAlive);
        }  
      
        void InitializeIfNeeded()
        {
            if (m_System == null)
                m_System = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            if (m_Particles == null || m_Particles.Length < m_System.main.maxParticles)
                m_Particles = new [ParticleSystem.Particle](ParticleSystem.Particle.html)[m_System.main.maxParticles];
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

