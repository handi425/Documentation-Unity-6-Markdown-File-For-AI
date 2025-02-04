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

#  [SpeedTreeImporter](SpeedTreeImporter.html).enableSubsurface

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

[Switch to Manual](../Manual/class-SpeedTreeImporter.html "Go to
SpeedTreeImporter Component in the Manual")

public bool[] enableSubsurface;

### Description

Gets and sets an array of booleans to enable the subsurface scattering effect
for each LOD (affects only SpeedTree v8 assets).

This setting controls the light scattered out the back side of leaves and
other two-sided SpeedTree materials. Because the subsurface scattering effect
comes with an increased performance cost, you may want to enable it only on
the SpeedTree assets that are nearest to the player. You can improve
performance by disabling the subsurface scattering effect on less detailed LOD
levels where the models are far enough away from the camera that the absence
of this effect is not noticeable. The array length that you supply must match
the number of LOD levels in your SpeedTree asset and typically has true values
at the start and false values at the end. For example, if your SpeedTree asset
has three LOD levels, you might pass an array of `[ true, true, false ]` to
enable the subsurface scattering effect on the first two LOD levels, but
disable it on the third.

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

