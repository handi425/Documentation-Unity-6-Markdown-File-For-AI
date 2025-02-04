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

# TriggerModule

struct in UnityEngine

/

Implemented
in:[UnityEngine.ParticleSystemModule](UnityEngine.ParticleSystemModule.html)

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

### Description

Script interface for the TriggerModule.

This module is useful for killing particles when they touch a set of collision
shapes, or for calling a script command to let you apply custom particle
behaviors when the trigger is activated.  
  
The example code for
[MonoBehaviour.OnParticleTrigger](MonoBehaviour.OnParticleTrigger.html) shows
how the callback type action works.  
  
Additional resources: [ParticleSystem](ParticleSystem.html),
[ParticleSystem.trigger](ParticleSystem-trigger.html).

### Properties

[colliderCount](ParticleSystem.TriggerModule-colliderCount.html)| Indicates
the number of collision shapes attached to this Particle System trigger.  
---|---  
[colliderQueryMode](ParticleSystem.TriggerModule-colliderQueryMode.html)|
Determines whether collider information is available when calling
[[ParticleSystem::GetTriggerParticles]].  
[enabled](ParticleSystem.TriggerModule-enabled.html)| Specifies whether the
TriggerModule is enabled or disabled.  
[enter](ParticleSystem.TriggerModule-enter.html)| Choose what action to
perform when particles enter the trigger volume.  
[exit](ParticleSystem.TriggerModule-exit.html)| Choose what action to perform
when particles leave the trigger volume.  
[inside](ParticleSystem.TriggerModule-inside.html)| Choose what action to
perform when particles are inside the trigger volume.  
[outside](ParticleSystem.TriggerModule-outside.html)| Choose what action to
perform when particles are outside the trigger volume.  
[radiusScale](ParticleSystem.TriggerModule-radiusScale.html)| A multiplier
Unity applies to the size of each particle before it processes overlaps.  
  
### Public Methods

[AddCollider](ParticleSystem.TriggerModule.AddCollider.html)| Adds a Collision
shape associated with this Particle System trigger.  
---|---  
[GetCollider](ParticleSystem.TriggerModule.GetCollider.html)| Gets a collision
shape associated with this Particle System trigger.  
[RemoveCollider](ParticleSystem.TriggerModule.RemoveCollider.html)| Removes a
collision shape associated with this Particle System trigger.  
[SetCollider](ParticleSystem.TriggerModule.SetCollider.html)| Sets a Collision
shape associated with this Particle System trigger.  
  
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

