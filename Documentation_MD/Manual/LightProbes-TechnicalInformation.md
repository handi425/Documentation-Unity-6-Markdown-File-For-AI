[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/LightProbes-TechnicalInformation.html)
  * [中文](/cn/current/Manual/LightProbes-TechnicalInformation.html)
  * [日本語](/ja/current/Manual/LightProbes-TechnicalInformation.html)
  * [한국어](/kr/current/Manual/LightProbes-TechnicalInformation.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/LightProbes-TechnicalInformation.html)
  * [中文](/cn/current/Manual/LightProbes-TechnicalInformation.html)
  * [日本語](/ja/current/Manual/LightProbes-TechnicalInformation.html)
  * [한국어](/kr/current/Manual/LightProbes-TechnicalInformation.html)

  * [Lighting](LightingOverview.html)
  * [Direct and indirect lighting](direct-and-indirect-lighting.html)
  * [Lighting data](Lightmap-data-landing.html)
  * Light Probe data format

[](Lightmaps-TechnicalInformation.html)

Lightmap data format

[](Lightmapping-landing.html)

Precalculating surface lighting with lightmaps

# Light Probe data format

The lighting information in the **light probes** Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) are encoded as Spherical Harmonics
basis functions. We use third order polynomials, also known as L2 Spherical
Harmonics. These are stored using 27 floating point values, 9 for each color
channel.

The **Enlighten** A lighting system by Geomerics used in Unity for Enlighten
Realtime Global Illumination. [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) implementation in Unity
uses a different spherical harmonics approach than Geomerics, the feature’s
original developer, namely the notation and reconstruction method from Peter-
Pike Sloan’s paper, [Stupid Spherical Harmonics (SH)
Tricks](http://www.ppsloan.org/publications/StupidSH36.pdf). Geomerics’
original approach was based on the notation and reconstruction method from
Ramamoorthi/Hanrahan’s paper, [An Efﬁcient Representation for Irradiance
Environment Maps](http://cseweb.ucsd.edu/~ravir/papers/envmap/envmap.pdf).

The **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) code for reconstruction is found in
UnityCG.cginc and is using the method from Appendix A10 Shader/CPU code for
Irradiance Environment Maps from Peter-Pikes paper.

The data is internally ordered like this:

    
    
                            [L00:  DC]
    
                [L1-1:  y] [L10:   z] [L11:   x]
    
      [L2-2: xy] [L2-1: yz] [L20:  zz] [L21:  xz]  [L22:  xx - yy]
    

The 9 coefficients for R, G and B are ordered like this:

    
    
    L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22, // red channel
    
    L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22, // blue channel
    
    L00, L1-1,  L10,  L11, L2-2, L2-1,  L20,  L21,  L22  // green channel
    

For more “under-the-hood” information about Unity’s light probe system, you
can read Robert Cupisz’s talk from GDC 2012, [Light Probe Interpolation Using
Tetrahedral Tessellations”, GDC 2012](http://gdcvault.com/play/1015312/Light-
Probe-Interpolation-Using-Tetrahedral)

* * *

  * 2017–06–08 Page published 

  * Light Probes updated in 5.6

[](Lightmaps-TechnicalInformation.html)

Lightmap data format

[](Lightmapping-landing.html)

Precalculating surface lighting with lightmaps

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

