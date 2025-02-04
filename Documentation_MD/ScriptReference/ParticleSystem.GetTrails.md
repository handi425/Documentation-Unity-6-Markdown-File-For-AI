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

#  [ParticleSystem](ParticleSystem.html).GetTrails

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

public [ParticleSystem.Trails](ParticleSystem.Trails.html) GetTrails();

### Returns

**Trails** The variable to populate with the Trails that currently belong to
the Particle System..

### Description

Returns all the data relating to the current internal state of the Particle
System Trails.

If you want to restore the Particle System to its current state in the future,
store the Trails this function returns along with
[ParticleSystem.GetParticles](ParticleSystem.GetParticles.html) and
[ParticleSystem.GetPlaybackState](ParticleSystem.GetPlaybackState.html).  
  
Additional resources: [Trails](ParticleSystem.Trails.html),
[SetTrails](ParticleSystem.SetTrails.html),
[GetPlaybackState](ParticleSystem.GetPlaybackState.html).

* * *

## Declaration

public int GetTrails(ref [ParticleSystem.Trails](ParticleSystem.Trails.html)
trailData);

### Parameters

trailData | The current Trails belonging to the Particle System.  
---|---  
  
### Returns

**int** The number of trails.

### Description

If you want to restore the Particle System to its current state in the future,
store the Trails this function returns along with
[ParticleSystem.GetParticles](ParticleSystem.GetParticles.html) and
[ParticleSystem.GetPlaybackState](ParticleSystem.GetPlaybackState.html).  
  
This method allows you to get the trail data without creating any garbage, if
you presize the trail data.  
  
Additional resources: [Trails](ParticleSystem.Trails.html),
[SetTrails](ParticleSystem.SetTrails.html),
[GetPlaybackState](ParticleSystem.GetPlaybackState.html).

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

