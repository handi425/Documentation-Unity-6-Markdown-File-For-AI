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

#  [MonoBehaviour](MonoBehaviour.html).OnParticleUpdateJobScheduled()

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

OnParticleUpdateJobScheduled is called when a Particle System's built-in
update job has been scheduled.

This can be used to attach custom managed jobs to run after the default
particle update.

    
    
    using UnityEngine;
    using UnityEngine.ParticleSystemJobs;  
      
    public class JobScript : [MonoBehaviour](MonoBehaviour.html)
    {
        void OnParticleUpdateJobScheduled()
        {
            [ParticleSystem](ParticleSystem.html) ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            new UpdateParticlesJob { m_DeltaTime = [Time.deltaTime](Time-deltaTime.html) }.Schedule(ps);
        }  
      
        struct UpdateParticlesJob : [IJobParticleSystem](ParticleSystemJobs.IJobParticleSystem.html)
        {
            public float m_DeltaTime;  
      
            public void Execute([ParticleSystemJobData](ParticleSystemJobs.ParticleSystemJobData.html) particles)
            {
                var positionsY = particles.positions.x;  
      
                for (int i = 0; i < particles.count; i++)
                {
                    positionsY[i] += 3.0f * m_DeltaTime;
                }
            }
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

