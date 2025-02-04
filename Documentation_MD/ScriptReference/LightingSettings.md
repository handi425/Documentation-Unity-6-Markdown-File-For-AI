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

# LightingSettings

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

[Switch to Manual](../Manual/class-LightingSettings.html "Go to
LightingSettings Component in the Manual")

### Description

An object containing settings for precomputing lighting data, that Unity can
serialize as a [Lighting Settings Asset](../Manual/class-
LightingSettings.html).

When the Unity Editor precomputes lighting data for a Scene that uses the
Baked Global Illumination system or the Enlighten Realtime Global Illumination
system, it uses settings from a `LightingSettings` object. The same
`LightingSettings` object can be assigned to more than one Scene, which makes
it possible to share settings across multiple Scenes.  
  
The following example shows how to create a `LightingSettings` object and
assign it to the active Scene using the
[Lightmapping.lightingSettings](Lightmapping-lightingSettings.html) API:

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateLightingSettingsExample
    {
        [[MenuItem](MenuItem.html)("Example/Create Lighting [Settings](Rendering.RayTracingAccelerationStructure.Settings.html)")]
        static void CreateExampleLightingSettings()
        {
            // Create an instance of [LightingSettings](LightingSettings.html)
            [LightingSettings](LightingSettings.html) lightingSettings = new [LightingSettings](LightingSettings.html)();  
      
            // Configure the [LightingSettings](LightingSettings.html) object
            lightingSettings.albedoBoost = 8.0f;  
      
            // Assign the [LightingSettings](LightingSettings.html) object to the active [Scene](SceneManagement.Scene.html)
            [Lightmapping.lightingSettings](Lightmapping-lightingSettings.html) = lightingSettings;
        }
    }
    

The following example shows how to create a `LightingSettings` object, and
save it to disk as a Lighting Settings Asset using the
[AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html) API.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateLightingSettingsExample
    {
        [[MenuItem](MenuItem.html)("Example/Create Lighting [Settings](Rendering.RayTracingAccelerationStructure.Settings.html)")]
        static void SaveExampleLightingSettingsToDisk()
        {
            // Create an instance of [LightingSettings](LightingSettings.html)
            [LightingSettings](LightingSettings.html) lightingSettings = new [LightingSettings](LightingSettings.html)();  
      
            // Configure the [LightingSettings](LightingSettings.html) object
            lightingSettings.albedoBoost = 8.0f;  
      
            // Save it to your Project, using the .lighting extension
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(lightingSettings, "Assets/ExampleLightingSettings.lighting");
        }
    }
    

Additional resources: [Lighting Settings Asset](../Manual/class-
LightingSettings.html).

### Properties

[albedoBoost](LightingSettings-albedoBoost.html)| The intensity of surface
albedo throughout the Scene when considered in lighting calculations. This
value influences the energy of light at each bounce. (Editor only).  
---|---  
[ao](LightingSettings-ao.html)| Whether to apply ambient occlusion to
lightmaps. (Editor only).  
[aoExponentDirect](LightingSettings-aoExponentDirect.html)| Determines the
degree to which direct lighting is considered when calculating ambient
occlusion in lightmaps. (Editor only).  
[aoExponentIndirect](LightingSettings-aoExponentIndirect.html)| Sets the
contrast of ambient occlusion that Unity applies to indirect lighting in
lightmaps. (Editor only).  
[aoMaxDistance](LightingSettings-aoMaxDistance.html)| The distance that a ray
travels before Unity considers it to be unoccluded when calculating ambient
occlusion in lightmaps. (Editor only).  
[bakedGI](LightingSettings-bakedGI.html)| Whether to enable the Baked Global
Illumination system for this Scene.  
[denoiserTypeAO](LightingSettings-denoiserTypeAO.html)| Determines the type of
denoising that the Progressive Lightmapper applies to ambient occlusion in
lightmaps. (Editor only).  
[denoiserTypeDirect](LightingSettings-denoiserTypeDirect.html)| Determines the
denoiser that the Progressive Lightmapper applies to direct lighting. (Editor
only).  
[denoiserTypeIndirect](LightingSettings-denoiserTypeIndirect.html)| Determines
the denoiser that the Progressive Lightmapper applies to indirect lighting.
(Editor only).  
[directionalityMode](LightingSettings-directionalityMode.html)| Determines
whether the lightmapper should generate directional or non-directional
lightmaps. (Editor only).  
[directSampleCount](LightingSettings-directSampleCount.html)| Specifies the
number of samples the Progressive Lightmapper uses for direct lighting
calculations. (Editor only).  
[environmentImportanceSampling](LightingSettings-
environmentImportanceSampling.html)| Determines whether Progressive
Lightmappers use importance sampling when they sample environment lighting
while baking.  
[environmentSampleCount](LightingSettings-environmentSampleCount.html)|
Specifies the number of samples the Progressive Lightmapper uses when sampling
indirect lighting from the skybox. (Editor only).  
[extractAO](LightingSettings-extractAO.html)| Whether the Progressive
Lightmapper extracts Ambient Occlusion to a separate lightmap. (Editor only).  
[filteringAtrousPositionSigmaAO](LightingSettings-
filteringAtrousPositionSigmaAO.html)| Specifies the threshold the Progressive
Lightmapper uses to filter direct light stored in the lightmap when using the
A-Trous filter. (Editor only).  
[filteringAtrousPositionSigmaDirect](LightingSettings-
filteringAtrousPositionSigmaDirect.html)| Specifies the threshold the
Progressive Lightmapper uses to filter the indirect lighting component of the
lightmap when using the A-Trous filter. (Editor only).  
[filteringAtrousPositionSigmaIndirect](LightingSettings-
filteringAtrousPositionSigmaIndirect.html)| Specifies the radius the
Progressive Lightmapper uses to filter the ambient occlusion component in the
lightmap when you use the Gaussian filter. (Editor only).  
[filteringGaussianRadiusAO](LightingSettings-filteringGaussianRadiusAO.html)|
Specifies the radius the Progressive Lightmapper uses to filter the direct
lighting component of the lightmap when you use the Gaussian filter. (Editor
only).  
[filteringGaussianRadiusDirect](LightingSettings-
filteringGaussianRadiusDirect.html)| Specifies the radius the Progressive
Lightmapper uses to filter the indirect lighting component of the lightmap
when you use the Gaussian filter. (Editor only).  
[filteringGaussianRadiusIndirect](LightingSettings-
filteringGaussianRadiusIndirect.html)| Specifies the method that the
Progressive Lightmapper uses to reduce noise in lightmaps. (Editor only).  
[filteringMode](LightingSettings-filteringMode.html)| Specifies the filter
type that the Progressive Lightmapper uses for ambient occlusion. (Editor
only).  
[filterTypeAO](LightingSettings-filterTypeAO.html)| Specifies the filter
kernel that the Progressive Lightmapper uses for ambient occlusion. (Editor
only).  
[filterTypeDirect](LightingSettings-filterTypeDirect.html)| Specifies the
filter kernel that the Progressive Lightmapper uses for the direct lighting.
(Editor only).  
[filterTypeIndirect](LightingSettings-filterTypeIndirect.html)| Specifies
whether the Editor calculates the final global illumination light bounce at
the same resolution as the baked lightmap.  
[indirectResolution](LightingSettings-indirectResolution.html)| Defines the
number of texels that Enlighten Realtime Global Illumination uses per world
unit when calculating indirect lighting. (Editor only).  
[indirectSampleCount](LightingSettings-indirectSampleCount.html)| Specifies
the number of samples the Progressive Lightmapper uses for indirect lighting
calculations. (Editor only).  
[indirectScale](LightingSettings-indirectScale.html)| Multiplies the intensity
of of indirect lighting in lightmaps. (Editor only).  
[lightmapCompression](LightingSettings-lightmapCompression.html)| The level of
compression the Editor uses for lightmaps.  
[lightmapMaxSize](LightingSettings-lightmapMaxSize.html)| The maximum size in
pixels of an individual lightmap texture. (Editor only).  
[lightmapPadding](LightingSettings-lightmapPadding.html)| Sets the distance
(in texels) between separate UV tiles in lightmaps. (Editor only).  
[lightmapper](LightingSettings-lightmapper.html)| Determines which backend to
use for baking lightmaps in the Baked Global Illumination system. (Editor
only).  
[lightmapResolution](LightingSettings-lightmapResolution.html)| Defines the
number of texels to use per world unit when generating lightmaps.  
[lightProbeSampleCountMultiplier](LightingSettings-
lightProbeSampleCountMultiplier.html)| Specifies the number of samples to use
for Light Probes relative to the number of samples for lightmap texels.
(Editor only).  
[maxBounces](LightingSettings-maxBounces.html)| Stores the maximum number of
bounces the Progressive Lightmapper computes for indirect lighting. (Editor
only)  
[minBounces](LightingSettings-minBounces.html)| Stores the minimum number of
bounces the Progressive Lightmapper computes for indirect lighting. (Editor
only)  
[mixedBakeMode](LightingSettings-mixedBakeMode.html)| Sets the
MixedLightingMode that Unity uses for all Mixed Lights in the Scene. (Editor
only).  
[prioritizeView](LightingSettings-prioritizeView.html)| Whether the
Progressive Lightmapper prioritizes baking visible texels within the frustum
of the Scene view. (Editor only).  
[realtimeEnvironmentLighting](LightingSettings-
realtimeEnvironmentLighting.html)| Determines the lightmap that Unity stores
environment lighting in.  
[realtimeGI](LightingSettings-realtimeGI.html)| Whether to enable the
Enlighten Realtime Global Illumination system for this Scene.  
[respectSceneVisibilityWhenBakingGI](LightingSettings-
respectSceneVisibilityWhenBakingGI.html)| When Unity is precomputing or baking
Global Illumination, respect the Scene Visibility setting of a [[GameObject]
with a MeshRenderer or Terrain component.  
  
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

