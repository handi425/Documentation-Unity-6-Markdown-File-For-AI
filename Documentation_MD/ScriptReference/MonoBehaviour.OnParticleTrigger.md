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

#  [MonoBehaviour](MonoBehaviour.html).OnParticleTrigger()

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

[Switch to Manual](../Manual/class-MonoBehaviour.html "Go to MonoBehaviour
Component in the Manual")

### Description

OnParticleTrigger is called when any particles in a Particle System meet the
conditions in the trigger module.

This can be used to kill or modify particles that are inside or outside a
collision volume.

    
    
    using UnityEngine;
    using System.Collections;
    using System.Collections.Generic;  
      
    public class TriggerScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnParticleTrigger()
        {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            // particles
            List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> enter = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();
            List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> exit = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();  
      
            // get
            int numEnter = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Enter](ParticleSystemTriggerEventType.Enter.html), enter);
            int numExit = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Exit](ParticleSystemTriggerEventType.Exit.html), exit);  
      
            // iterate
            for (int i = 0; i < numEnter; i++)
            {
                [ParticleSystem.Particle](ParticleSystem.Particle.html) p = enter[i];
                p.startColor = new [Color32](Color32.html)(255, 0, 0, 255);
                enter[i] = p;
            }
            for (int i = 0; i < numExit; i++)
            {
                [ParticleSystem.Particle](ParticleSystem.Particle.html) p = exit[i];
                p.startColor = new [Color32](Color32.html)(0, 255, 0, 255);
                exit[i] = p;
            }  
      
            // set
            ps.SetTriggerParticles([ParticleSystemTriggerEventType.Enter](ParticleSystemTriggerEventType.Enter.html), enter);
            ps.SetTriggerParticles([ParticleSystemTriggerEventType.Exit](ParticleSystemTriggerEventType.Exit.html), exit);
        }
    }
    

In order to retrieve detailed information about all the collisions caused by
the [ParticleSystem](ParticleSystem.html),
[ParticlePhysicsExtensions.GetTriggerParticles](ParticlePhysicsExtensions.GetTriggerParticles.html)
must be used to retrieve the array of
[Particle](ParticleSystem.Particle.html).

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

