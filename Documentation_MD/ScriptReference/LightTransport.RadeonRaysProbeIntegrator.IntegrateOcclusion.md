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

#
[RadeonRaysProbeIntegrator](LightTransport.RadeonRaysProbeIntegrator.html).IntegrateOcclusion

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

[ ]()

## Declaration

public
[LightTransport.IProbeIntegrator.Result](LightTransport.IProbeIntegrator.Result.html)
IntegrateOcclusion([LightTransport.IDeviceContext](LightTransport.IDeviceContext.html)
context, int positionOffset, int positionCount, int sampleCount, int
maxLightsPerProbe, BufferSlice<int> perProbeLightIndices, BufferSlice<float>
probeOcclusionEstimateOut);

### Parameters

context | Device context.  
---|---  
positionOffset | Offset measured from the beginning of the probe position buffer.  
positionCount | Number of probes to integrate.  
sampleCount | Number of samples to take.  
maxLightsPerProbe | Maximum number of lights per probe. The value must be 4.  
perProbeLightIndices | Buffer slice containing the per probe light indices.  
probeOcclusionEstimateOut | Buffer slice to write the probe occlusion estimate into. The size of the buffer in bytes should be maxLightsPerProbe * sizeof(float).  
  
### Returns

**Result** Return code.

### Description

Integrate occlusion.

The integrator does spherical sampling for each probe position. Occlusion is 1
if all rays hit front-facing triangles or the sky. Occlusion is 0 if all rays
hit back-facing triangles.  
  
Additional resources:
[InputExtraction.ComputeOcclusionLightIndicesFromBakeInput](LightTransport.InputExtraction.ComputeOcclusionLightIndicesFromBakeInput.html).

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

