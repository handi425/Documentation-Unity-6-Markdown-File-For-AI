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

#  [SpeedTreeImporter](SpeedTreeImporter.html).selectedWindQuality

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

public int selectedWindQuality;

### Description

Gets and sets an integer corresponding to the SpeedTreeWind enum values. The
value is clamped by [SpeedTreeImporter.bestWindQuality](SpeedTreeImporter-
bestWindQuality.html) internally.

The possible wind quality values are as follows:  
  
`0` \- Off  
`1` \- Fastest  
`2` \- Fast  
`3` \- Better  
`4` \- Best  
`5` \- Palm (only available on palm-like trees)  
  
The SpeedTree Modeler determines the
[SpeedTreeImporter.bestWindQuality](SpeedTreeImporter-bestWindQuality.html)
value, which is then used to limit the available `selectedWindQuality` values.
You can lower the wind quality of a SpeedTree model in the Unity Editor based
on the application's needs, but you can't improve the wind quality without the
SpeedTree Modeler, which generates the necessary wind data in the SpeedTree
model file during the export process.  
  
To change this setting for a specific LOD, see
[SpeedTreeImporter.windQualities](SpeedTreeImporter-windQualities.html) and
[SpeedTreeImporter.enableSettingOverride](SpeedTreeImporter-
enableSettingOverride.html).

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

