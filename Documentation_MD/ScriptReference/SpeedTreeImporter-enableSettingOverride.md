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

#  [SpeedTreeImporter](SpeedTreeImporter.html).enableSettingOverride

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

public bool[] enableSettingOverride;

### Description

Gets and sets an array of booleans to customize importer settings for a
specific LOD.

The number of elements in this array must match the number of LODs in the
model.  
  
The following are the per-LOD settings:

  * `enableSettingOverride`
  * [SpeedTreeImporter.LODHeights](SpeedTreeImporter.LODHeights.html)
  * [SpeedTreeImporter.castShadows](SpeedTreeImporter-castShadows.html)
  * [SpeedTreeImporter.receiveShadows](SpeedTreeImporter-receiveShadows.html)
  * [SpeedTreeImporter.useLightProbes](SpeedTreeImporter-useLightProbes.html)
  * [SpeedTreeImporter.enableBump](SpeedTreeImporter-enableBump.html)
  * [SpeedTreeImporter.enableHue](SpeedTreeImporter-enableHue.html)
  * [SpeedTreeImporter.enableSubsurface](SpeedTreeImporter-enableSubsurface.html)
  * [SpeedTreeImporter.windQualities](SpeedTreeImporter-windQualities.html)

When a boolean in this array is set to `true`,
[SpeedTreeImporter](SpeedTreeImporter.html) generates an additional material
with the specified per-LOD settings and the corresponding LOD index. You can
use these settings to fine-tune the performance of the application, but
consider that additional material generation comes with certain CPU and GPU
performance trade-offs. It is recommended to use settings override together
with performance profiling tools to ensure meaningful performance gains.  
  
When the setting override for an LOD is not enabled, the material and mesh
properties of the imported SpeedTree asset have the following settings:

  * [SpeedTreeImporter.castShadowsByDefault](SpeedTreeImporter-castShadowsByDefault.html)
  * [SpeedTreeImporter.receiveShadowsByDefault](SpeedTreeImporter-receiveShadowsByDefault.html)
  * [SpeedTreeImporter.useLightProbesByDefault](SpeedTreeImporter-useLightProbesByDefault.html)
  * [SpeedTreeImporter.enableBumpByDefault](SpeedTreeImporter-enableBumpByDefault.html)
  * [SpeedTreeImporter.enableHueByDefault](SpeedTreeImporter-enableHueByDefault.html)
  * [SpeedTreeImporter.enableSubsurfaceByDefault](SpeedTreeImporter-enableSubsurfaceByDefault.html)
  * [SpeedTreeImporter.selectedWindQuality](SpeedTreeImporter-selectedWindQuality.html)

In other words, the `enableSettingOverride` overrides the '*ByDefault'
settings for a specific LOD level with the values in the per-LOD settings.  
  

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

