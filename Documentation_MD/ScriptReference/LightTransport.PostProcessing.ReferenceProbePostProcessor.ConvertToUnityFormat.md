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
[ReferenceProbePostProcessor](LightTransport.PostProcessing.ReferenceProbePostProcessor.html).ConvertToUnityFormat

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

public bool
ConvertToUnityFormat([LightTransport.IDeviceContext](LightTransport.IDeviceContext.html)
context, BufferSlice<SphericalHarmonicsL2> irradianceIn,
BufferSlice<SphericalHarmonicsL2> irradianceOut, int probeCount);

### Parameters

context | Device context.  
---|---  
irradianceIn | Buffer containing input irradiance.  
irradianceOut | Output buffer containing the irradiance array after the conversion to the format compatible with a Unity renderer.  
probeCount | Number of SphericalHarmonicsL2 probes to convert.  
  
### Returns

**bool** True if the operation was successfully added to the command queue on
the context.

### Description

Converts light probes encoded as
[SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html) to the format
expected by the Unity renderer.

The irradiance [SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html)
light probes must satisfy the following conditions when used with a Unity
renderer: 1) For L0 and L1, the coefficients must have the SH standard
normalization terms folded into them (to avoid doing this multiplication in a
shader). 2) The coefficients must be divided by Pi (π) for compatibility
reasons. 3) L1 must be ordered as yzx (rather than xyz). The order is flipped
back right before rendering in the GetShaderConstantsFromNormalizedSH
function, before the
[SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html) probes are passed
to a shader.

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

