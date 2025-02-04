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

#  [LightingSettings](LightingSettings.html).maxBounces

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

[Switch to Manual](../Manual/class-LightingSettings.html "Go to
LightingSettings Component in the Manual")

public int maxBounces;

### Description

Stores the maximum number of bounces the Progressive Lightmapper computes for
indirect lighting. (Editor only)

To reduce the computational load and improve performance during bakes, the
Progressive Lightmapper terminates light paths that contribute little to the
appearance of the Scene lighting. Light paths are weighted so that those with
low intensity are more likely to be terminated first. This technique is known
as Russian Roulette.  
  
`maxBounces` determines the maximum number of bounces for an indirect light
path.  
  
Default value: 2. Range: 0–100. The higher the value, the longer the bake
time. Values of up to 10 are suitable for most Scenes. Values higher than 10
might lead to significantly longer bake times.  
  
To disable the Russian Roulette technique, set `maxBounces` to the same value
as LightmapSettings.minBounces.  
  
When Unity serializes this `LightingSettings` object as a [Lighting Settings
Asset](../Manual/class-LightingSettings.html), this property corresponds to
the **Max Bounces** property in the Lighting Settings Asset Inspector.  
  
Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html), LightmapSettings.minBounces.

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

