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

#  [Mesh](Mesh.html).RecalculateUVDistributionMetric

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public void RecalculateUVDistributionMetric(int uvSetIndex, float
uvAreaThreshold);

### Parameters

uvSetIndex | The UV set index to set the UV distibution metric for. Use 0 for first index.  
---|---  
uvAreaThreshold | The minimum UV area to consider. The default value is 1e-9f.  
  
### Description

Recalculates the UV distribution metric of the Mesh from the vertices and uv
coordinates.

The UV distribution metric can be used to calculate the desired mipmap level
based on the position of the camera. It's important to call this function
after procedurally generating meshes that have textures that use [Mip Map
Streaming](../Manual/TextureStreaming.html).  
  
This function can also be used to update the UV distribution metric with an
alternative uvAreaThreshold. The uvAreaThreshold can be used to ignore small
UV areas from the UV distribution calculation; for example, you may wish to
ignore a single texel colour used for a large triangle area. Unity will not
consider the density of these areas when calculating mip selection, which may
result in some colour tint due to lower mips being selected. The value depends
on the texture resolution; for example, for a 256x256 texture, a single texel
area would be (1/(256*256)).  
  
Additional resources: [Mip Map Streaming](../Manual/TextureStreaming.html)
[GetUVDistributionMetric](Mesh.GetUVDistributionMetric.html),
[RecalculateUVDistributionMetrics](Mesh.RecalculateUVDistributionMetrics.html).

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

