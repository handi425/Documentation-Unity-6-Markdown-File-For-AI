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

# LightmapParameters

class in UnityEditor

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-LightmapParameters.html "Go to
LightmapParameters Component in the Manual")

### Description

Configures how Unity bakes lighting and can be assigned to a
[LightingSettings](LightingSettings.html) instance or asset.

Note that Unity's built-in Lightmap Parameters Assets are read-only.  
  
Additional resources:
[LightmapParameters.SetLightmapParametersForLightingSettings](LightmapParameters.SetLightmapParametersForLightingSettings.html).

### Properties

[antiAliasingSamples](LightmapParameters-antiAliasingSamples.html)| The kernel
width the lightmapper uses when sampling a lightmap texel.  
---|---  
[AOAntiAliasingSamples](LightmapParameters.AOAntiAliasingSamples.html)| The
maximum number of times to supersample a texel to reduce aliasing in AO.  
[AOQuality](LightmapParameters.AOQuality.html)| The number of rays to cast for
computing ambient occlusion.  
[backFaceTolerance](LightmapParameters-backFaceTolerance.html)| The percentage
of rays shot from a ray origin that must hit front faces to be considered
usable.  
[bakedLightmapTag](LightmapParameters-bakedLightmapTag.html)| BakedLightmapTag
is an integer that affects the assignment to baked lightmaps. Objects with
different values for bakedLightmapTag are guaranteed to not be assigned to the
same lightmap even if the other baking parameters are the same.  
[blurRadius](LightmapParameters-blurRadius.html)| The radius (in texels) of
the post-processing filter that blurs baked direct lighting.  
[clusterResolution](LightmapParameters-clusterResolution.html)| Controls the
resolution at which Enlighten Realtime Global Illumination stores and can
transfer input light.  
[directLightQuality](LightmapParameters-directLightQuality.html)| The number
of rays used for lights with an area. Allows for accurate soft shadowing.  
[irradianceBudget](LightmapParameters-irradianceBudget.html)| The amount of
data used for Enlighten Realtime Global Illumination texels. Specifies how
detailed view of the Scene a texel has. Small values mean more averaged out
lighting.  
[irradianceQuality](LightmapParameters-irradianceQuality.html)| The number of
rays to cast for computing irradiance form factors.  
[isTransparent](LightmapParameters-isTransparent.html)| If enabled, the object
appears transparent during GlobalIllumination lighting calculations.  
[limitLightmapCount](LightmapParameters-limitLightmapCount.html)| If enabled,
objects sharing the same lightmap parameters will be packed into
LightmapParameters.maxLightmapCount lightmaps.  
[maxLightmapCount](LightmapParameters-maxLightmapCount.html)| The maximum
number of lightmaps created for objects sharing the same lightmap parameters.
This property is ignored if LightmapParameters.limitLightmapCount is false.  
[modellingTolerance](LightmapParameters-modellingTolerance.html)| Maximum size
of gaps that can be ignored for GI (multiplier on pixel size).  
[pushoff](LightmapParameters-pushoff.html)| The distance to offset the ray
origin from the geometry when performing ray tracing, in modelling units.
Unity applies the offset to all baked lighting: direct lighting, indirect
lighting, environment lighting and ambient occlusion.  
[resolution](LightmapParameters-resolution.html)| The texel resolution per
meter used for real-time lightmaps. This value is multiplied by
LightingSettings.indirectResolution.  
[stitchEdges](LightmapParameters-stitchEdges.html)| Whether pairs of edges
should be stitched together.  
[systemTag](LightmapParameters-systemTag.html)| System tag is an integer
identifier. It lets you force an object into a different Enlighten Realtime
Global Illumination system even though all the other parameters are the same.  
  
### Public Methods

[AssignToLightingSettings](LightmapParameters.AssignToLightingSettings.html)|
Assignes itself to a LightingSettings instance or asset.  
---|---  
  
### Static Methods

[GetLightmapParametersForLightingSettings](LightmapParameters.GetLightmapParametersForLightingSettings.html)|
Returns the assigned LightmapParameters for the specified LightingSettings.  
---|---  
[SetLightmapParametersForLightingSettings](LightmapParameters.SetLightmapParametersForLightingSettings.html)|
Sets the LightmapParameters for the specified LightingSettings.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

