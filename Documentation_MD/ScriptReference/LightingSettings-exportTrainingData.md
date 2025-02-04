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

**Method group is Obsolete**  

#  [LightingSettings](LightingSettings.html).exportTrainingData

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

**Obsolete** Training data export for baked lighting is deprecated. public
bool exportTrainingData;

### Description

Whether the Progressive Lightmapper exports machine learning training data to
the Project folder when it performs the bake. ( Editor only).

When this is set to `true`, the Progressive Lightmapper exports separate data
for direct lighting, indirect lighting, directionality, Ambient Occlusion,
Texel Validity, normals, positions, albedo, emission, a coverage mask, and the
final lightmap. This data is useful when training machine learning (ML)
networks When this is set to `false`, the Progressive Lightmapper does not
export this data.  
  
The direct and indirect textures are exported before filtering, but after
markup of invalid texels. The lightmap and directionality are exported after
filtering and compositing. Ambient Occlusion exports with an exponent of 1. It
does not take the indirect/direct exponent into account. To be able to export
valid data for Directionality and Ambient Occlusion, they must first be
enabled.  
  
Normals and positions are exported in both object space (os) and world space
(ws). Normals are normalized, positions are not. Some textures are marked as
"supersampled". This means that the Editor exports the values without
downsampling them, if they have a supersampling multiplier that is higher than
1.  
  
All textures have the coverage mask as their alpha channel.  
  
To change the name of the export folder, see
[trainingDataDestination](LightingSettings-trainingDataDestination.html).  
  
Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html), [trainingDataDestination](LightingSettings-
trainingDataDestination.html).

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

