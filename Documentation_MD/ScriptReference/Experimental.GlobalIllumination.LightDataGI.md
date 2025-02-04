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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# LightDataGI

struct in UnityEngine.Experimental.GlobalIllumination

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

The interop structure to pass light information to the light baking backends.
There are helper structures for Directional, Point, Spot and Rectangle lights
to correctly initialize this structure.

### Properties

[color](Experimental.GlobalIllumination.LightDataGI-color.html)| The color of
the light.  
---|---  
[coneAngle](Experimental.GlobalIllumination.LightDataGI-coneAngle.html)| The
cone angle for spot lights.  
[cookieID](Experimental.GlobalIllumination.LightDataGI-cookieID.html)| The
cookie texture's instance id projected by the light.  
[cookieScale](Experimental.GlobalIllumination.LightDataGI-cookieScale.html)|
The uniform scale factor for downscaling cookies during lightmapping. Can be
used as an optimization when full resolution cookies are not needed for
indirect lighting.  
[falloff](Experimental.GlobalIllumination.LightDataGI-falloff.html)| The
falloff model to use for baking point and spot lights.  
[indirectColor](Experimental.GlobalIllumination.LightDataGI-
indirectColor.html)| The indirect color of the light.  
[innerConeAngle](Experimental.GlobalIllumination.LightDataGI-
innerConeAngle.html)| The inner cone angle for spot lights.  
[instanceID](Experimental.GlobalIllumination.LightDataGI-instanceID.html)| The
light's instanceID.  
[mode](Experimental.GlobalIllumination.LightDataGI-mode.html)| The lightmap
mode for the light.  
[orientation](Experimental.GlobalIllumination.LightDataGI-orientation.html)|
The orientation of the light.  
[position](Experimental.GlobalIllumination.LightDataGI-position.html)| The
position of the light.  
[range](Experimental.GlobalIllumination.LightDataGI-range.html)| The range of
the light. Unused for directional lights.  
[shadow](Experimental.GlobalIllumination.LightDataGI-shadow.html)| Set to 1
for shadow casting lights, 0 otherwise.  
[shape0](Experimental.GlobalIllumination.LightDataGI-shape0.html)| The light's
sphere radius for point and spot lights, or the width for rectangle lights.  
[shape1](Experimental.GlobalIllumination.LightDataGI-shape1.html)| The height
for rectangle lights.  
[type](Experimental.GlobalIllumination.LightDataGI-type.html)| The type of the
light.  
  
### Public Methods

[Init](Experimental.GlobalIllumination.LightDataGI.Init.html)| Initialize the
struct with the parameters from the given light type.  
---|---  
[InitNoBake](Experimental.GlobalIllumination.LightDataGI.InitNoBake.html)|
Initialize a light so that the baking backends ignore it.  
  
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

