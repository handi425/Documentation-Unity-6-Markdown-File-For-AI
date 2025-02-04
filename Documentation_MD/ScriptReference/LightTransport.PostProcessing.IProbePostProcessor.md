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

# IProbePostProcessor

interface in UnityEngine.LightTransport.PostProcessing

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

### Description

Interface for light probe post processing.

The interface provides common operations for light probes encoded as
[SphericalHarmonicsL2](Rendering.SphericalHarmonicsL2.html). Operations
include radiance to irradiance conversion, conversion to the format expected
by Unity for rendering (refer to
[IProbePostProcessor.ConvertToUnityFormat](LightTransport.PostProcessing.IProbePostProcessor.ConvertToUnityFormat.html)),
addition, and scaling.

### Public Methods

[AddSphericalHarmonicsL2](LightTransport.PostProcessing.IProbePostProcessor.AddSphericalHarmonicsL2.html)|
Add two arrays of SphericalHarmonicsL2 together.  
---|---  
[ConvertToUnityFormat](LightTransport.PostProcessing.IProbePostProcessor.ConvertToUnityFormat.html)|
Converts light probes encoded as SphericalHarmonicsL2 to the format expected
by the Unity renderer.  
[ConvolveRadianceToIrradiance](LightTransport.PostProcessing.IProbePostProcessor.ConvolveRadianceToIrradiance.html)|
Convolve radiance to irradiance.  
[DeringSphericalHarmonicsL2](LightTransport.PostProcessing.IProbePostProcessor.DeringSphericalHarmonicsL2.html)|
De-ring an array of SphericalHarmonicsL2 probes.  
[Initialize](LightTransport.PostProcessing.IProbePostProcessor.Initialize.html)|
Initialize the IProbePostProcessor.  
[ScaleSphericalHarmonicsL2](LightTransport.PostProcessing.IProbePostProcessor.ScaleSphericalHarmonicsL2.html)|
Scale an array of SphericalHarmonicsL2 probes.  
[WindowSphericalHarmonicsL2](LightTransport.PostProcessing.IProbePostProcessor.WindowSphericalHarmonicsL2.html)|
Apply a windowing operation on an array of SphericalHarmonicsL2 probes.  
  
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

