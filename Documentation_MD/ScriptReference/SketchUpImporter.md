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

# SketchUpImporter

class in UnityEditor

/

Inherits from:[ModelImporter](ModelImporter.html)

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

[Switch to Manual](../Manual/class-SketchUpImporter.html "Go to
SketchUpImporter Component in the Manual")

### Description

Derives from AssetImporter to handle importing of SketchUp files.

From the SketchUpImporter, you can access certain properties that are
extracted from the SketchUp file.  
  
The following is an example of showing the geo coordinate extracted from the
SketchUp file.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SketchUpUtility
    {
        public static void ShowGeoCoordinate([GameObject](GameObject.html) go)
        {
            string assetPath = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(go); // get asset path
            // get [SketchUpImporter](SketchUpImporter.html)
            [SketchUpImporter](SketchUpImporter.html) importer = [AssetImporter.GetAtPath](AssetImporter.GetAtPath.html)(assetPath) as [SketchUpImporter](SketchUpImporter.html);
            if (importer == null)
            {
                [Debug.Log](Debug.Log.html)("This object is not imported by [SketchUpImporter](SketchUpImporter.html)");
                return;
            }  
      
            [Debug.Log](Debug.Log.html)(string.Format("Lat:{0} Long:{1} NorthCorrection:{2}", importer.latitude, importer.longitude, importer.northCorrection));
        }
    }
    

### Properties

[latitude](SketchUpImporter-latitude.html)| Retrieves the latitude Geo
Coordinate imported from the SketchUp file.  
---|---  
[longitude](SketchUpImporter-longitude.html)| Retrieves the longitude Geo
Coordinate imported from the SketchUp file.  
[northCorrection](SketchUpImporter-northCorrection.html)| Retrieves the north
correction value imported from the SketchUp file.  
  
### Public Methods

[GetDefaultCamera](SketchUpImporter.GetDefaultCamera.html)| The default camera
or the camera of the active Scene which the SketchUp file was saved with.  
---|---  
[GetScenes](SketchUpImporter.GetScenes.html)| The method returns an array of
SketchUpImportScene which represents SketchUp scenes.  
  
### Inherited Members

### Properties

[assetBundleName](AssetImporter-assetBundleName.html)| Get or set the
AssetBundle name.  
---|---  
[assetBundleVariant](AssetImporter-assetBundleVariant.html)| Get or set the
AssetBundle variant.  
[assetPath](AssetImporter-assetPath.html)| The path name of the asset for this
importer. (Read Only)  
[importSettingsMissing](AssetImporter-importSettingsMissing.html)| The value
is true when no meta file is provided with the imported asset.  
[userData](AssetImporter-userData.html)| Get or set any user data.  
[addCollider](ModelImporter-addCollider.html)| Add mesh colliders to imported
meshes.  
[animationCompression](ModelImporter-animationCompression.html)| Animation
compression setting.  
[animationPositionError](ModelImporter-animationPositionError.html)| Allowed
error of animation position compression.  
[animationRotationError](ModelImporter-animationRotationError.html)| Allowed
error of animation rotation compression.  
[animationScaleError](ModelImporter-animationScaleError.html)| Allowed error
of animation scale compression.  
[animationType](ModelImporter-animationType.html)| Animator generation mode.  
[animationWrapMode](ModelImporter-animationWrapMode.html)| The default wrap
mode for the generated animation clips.  
[autoGenerateAvatarMappingIfUnspecified](ModelImporter-
autoGenerateAvatarMappingIfUnspecified.html)| Generate auto mapping if no
avatarSetup is provided when importing humanoid animation.  
[avatarSetup](ModelImporter-avatarSetup.html)| The Avatar generation of the
imported model.  
[bakeAxisConversion](ModelImporter-bakeAxisConversion.html)| Computes the axis
conversion on geometry and animation for Models defined in an axis system that
differs from Unity's (left handed, Z forward, Y-up). When enabled, Unity
transforms the geometry and animation data in order to convert the axis. When
disabled, Unity transforms the root GameObject of the hierarchy in order to
convert the axis.  
[bakeIK](ModelImporter-bakeIK.html)| Bake Inverse Kinematics (IK) when
importing.  
[clipAnimations](ModelImporter-clipAnimations.html)| Animation clips to split
animation into. Additional resources: ModelImporterClipAnimation.  
[defaultClipAnimations](ModelImporter-defaultClipAnimations.html)| Generate a
list of all default animation clip based on TakeInfo.  
[extraExposedTransformPaths](ModelImporter-extraExposedTransformPaths.html)|
Animation optimization setting.  
[extraUserProperties](ModelImporter-extraUserProperties.html)| A list of
default FBX properties to treat as user properties during
OnPostprocessGameObjectWithUserProperties.  
[fileScale](ModelImporter-fileScale.html)| Scaling factor used when
useFileScale is set to true (Read-only).  
[generateAnimations](ModelImporter-generateAnimations.html)| Animation
generation options.  
[generateSecondaryUV](ModelImporter-generateSecondaryUV.html)| Generate
secondary UV set for lightmapping.  
[globalScale](ModelImporter-globalScale.html)| Global scale factor for
importing.  
[humanDescription](ModelImporter-humanDescription.html)| The human description
that is used to generate an Avatar during the import process.  
[humanoidOversampling](ModelImporter-humanoidOversampling.html)| Controls how
much oversampling is used when importing humanoid animations for retargeting.  
[importAnimatedCustomProperties](ModelImporter-
importAnimatedCustomProperties.html)| Import animated custom properties from
file.  
[importAnimation](ModelImporter-importAnimation.html)| Import animation from
file.  
[importBlendShapeDeformPercent](ModelImporter-
importBlendShapeDeformPercent.html)| Import BlendShapes deform percent.  
[importBlendShapeNormals](ModelImporter-importBlendShapeNormals.html)| Blend
shape normal import options.  
[importBlendShapes](ModelImporter-importBlendShapes.html)| Controls import of
BlendShapes.  
[importCameras](ModelImporter-importCameras.html)| Controls import of cameras.
Basic properties like field of view, near plane distance and far plane
distance can be animated.  
[importConstraints](ModelImporter-importConstraints.html)| Import animation
constraints.  
[importedTakeInfos](ModelImporter-importedTakeInfos.html)| Generates the list
of all imported take.  
[importLights](ModelImporter-importLights.html)| Controls import of lights.
Note that because light are defined differently in DCC tools, some light types
or properties may not be exported. Basic properties like color and intensity
can be animated.  
[importNormals](ModelImporter-importNormals.html)| Vertex normal import
options.  
[importTangents](ModelImporter-importTangents.html)| Vertex tangent import
options.  
[importVisibility](ModelImporter-importVisibility.html)| Use visibility
properties to enable or disable MeshRenderer components.  
[indexFormat](ModelImporter-indexFormat.html)| Format of the imported mesh
index buffer data.  
[isBakeIKSupported](ModelImporter-isBakeIKSupported.html)| Is Bake Inverse
Kinematics (IK) supported by this importer.  
[isReadable](ModelImporter-isReadable.html)| Are mesh vertices and indices
accessible from script?  
[isTangentImportSupported](ModelImporter-isTangentImportSupported.html)| Is
import of tangents supported by this importer.  
[isUseFileUnitsSupported](ModelImporter-isUseFileUnitsSupported.html)| Is
useFileUnits supported for this asset.  
[keepQuads](ModelImporter-keepQuads.html)| If this is true, any quad faces
that exist in the mesh data before it is imported are kept as quads instead of
being split into two triangles, for the purposes of tessellation. Set this to
false to disable this behavior.  
[materialImportMode](ModelImporter-materialImportMode.html)| Material creation
options.  
[materialLocation](ModelImporter-materialLocation.html)| Material import
location options.  
[materialName](ModelImporter-materialName.html)| Material naming setting.  
[materialSearch](ModelImporter-materialSearch.html)| Existing material search
setting.  
[maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html)| The maximum number
of bones per vertex stored in this mesh data.  
[meshCompression](ModelImporter-meshCompression.html)| Mesh compression
setting.  
[meshOptimizationFlags](ModelImporter-meshOptimizationFlags.html)| Options to
control the optimization of mesh data during asset import.  
[minBoneWeight](ModelImporter-minBoneWeight.html)| Minimum bone weight to
keep.  
[motionNodeName](ModelImporter-motionNodeName.html)| The path of the transform
used to generation the motion of the animation.  
[normalCalculationMode](ModelImporter-normalCalculationMode.html)| Normal
generation options for ModelImporter.  
[normalSmoothingAngle](ModelImporter-normalSmoothingAngle.html)| Smoothing
angle (in degrees) for calculating normals.  
[normalSmoothingSource](ModelImporter-normalSmoothingSource.html)| Source of
smoothing information for calculation of normals.  
[optimizeBones](ModelImporter-optimizeBones.html)| Only import bones where
they are connected to vertices.  
[optimizeGameObjects](ModelImporter-optimizeGameObjects.html)| Animation
optimization setting.  
[optimizeMeshPolygons](ModelImporter-optimizeMeshPolygons.html)| Optimize the
order of polygons in the mesh to make better use of the GPUs internal caches
to improve rendering performance.  
[optimizeMeshVertices](ModelImporter-optimizeMeshVertices.html)| Optimize the
order of vertices in the mesh to make better use of the GPUs internal caches
to improve rendering performance.  
[preserveHierarchy](ModelImporter-preserveHierarchy.html)| If true, always
create an explicit Prefab root. Otherwise, if the model has a single root, it
is reused as the Prefab root.  
[referencedClips](ModelImporter-referencedClips.html)| Returns the matching
referenced clip assets for this model.  
[removeConstantScaleCurves](ModelImporter-removeConstantScaleCurves.html)|
Removes constant animation curves with values identical to the object initial
scale value.  
[resampleCurves](ModelImporter-resampleCurves.html)| If set to false, the
importer will not resample curves when possible. Read more about animation
curve resampling.Notes:- Some unsupported FBX features (such as PreRotation or
PostRotation on transforms) will override this setting. In these situations,
animation curves will still be resampled even if the setting is disabled. For
best results, avoid using PreRotation, PostRotation and GetRotationPivot.-
This option was introduced in Version 5.3. Prior to this version, Unity's
import behaviour was as if this option was always enabled. Therefore enabling
the option gives the same behaviour as pre-5.3 animation import.  
[secondaryUVAngleDistortion](ModelImporter-secondaryUVAngleDistortion.html)|
Threshold for angle distortion (in degrees) when generating secondary UV.  
[secondaryUVAreaDistortion](ModelImporter-secondaryUVAreaDistortion.html)|
Threshold for area distortion when generating secondary UV.  
[secondaryUVHardAngle](ModelImporter-secondaryUVHardAngle.html)| Hard angle
(in degrees) for generating secondary UV.  
[secondaryUVMarginMethod](ModelImporter-secondaryUVMarginMethod.html)| Method
to use for handling margins when generating secondary UV.  
[secondaryUVMinLightmapResolution](ModelImporter-
secondaryUVMinLightmapResolution.html)| The minimum lightmap resolution in
texels per unit that the associated model is expected to have.  
[secondaryUVMinObjectScale](ModelImporter-secondaryUVMinObjectScale.html)| The
minimum object scale that the associated model is expected to have.  
[secondaryUVPackMargin](ModelImporter-secondaryUVPackMargin.html)| Margin to
be left between charts when packing secondary UV.  
[skinWeights](ModelImporter-skinWeights.html)| Skin weights import options.  
[sortHierarchyByName](ModelImporter-sortHierarchyByName.html)| Sorts the
gameObject hierarchy by name.  
[sourceAvatar](ModelImporter-sourceAvatar.html)| Imports the HumanDescription
from the given Avatar.  
[strictVertexDataChecks](ModelImporter-strictVertexDataChecks.html)| Enables
strict checks on imported vertex data.  
[swapUVChannels](ModelImporter-swapUVChannels.html)| Swap primary and
secondary UV channels when importing.  
[transformPaths](ModelImporter-transformPaths.html)| Generates the list of all
imported Transforms.  
[useFileScale](ModelImporter-useFileScale.html)| Use FileScale when importing.  
[useFileUnits](ModelImporter-useFileUnits.html)| Detect file units and import
as 1FileUnit=1UnityUnit, otherwise it will import as 1cm=1UnityUnit.  
[useSRGBMaterialColor](ModelImporter-useSRGBMaterialColor.html)| When
disabled, imported material albedo colors are converted to gamma space. This
property should be disabled when using linear color space in Player rendering
settings. The default value is true.  
[weldVertices](ModelImporter-weldVertices.html)| Combine vertices that share
the same position in space.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[AddRemap](AssetImporter.AddRemap.html)| Map a sub-asset from an imported
asset (such as an FBX file) to an external Asset of the same type.  
---|---  
[GetExternalObjectMap](AssetImporter.GetExternalObjectMap.html)| Gets a copy
of the external object map used by the AssetImporter.  
[RemoveRemap](AssetImporter.RemoveRemap.html)| Removes an item from the map of
external objects.  
[SaveAndReimport](AssetImporter.SaveAndReimport.html)| Save asset importer
settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](AssetImporter.SetAssetBundleNameAndVariant.html)|
Set the AssetBundle name and variant.  
[SupportsRemappedAssetType](AssetImporter.SupportsRemappedAssetType.html)|
Checks if the AssetImporter supports remapping the given asset type.  
[CreateDefaultMaskForClip](ModelImporter.CreateDefaultMaskForClip.html)|
Creates a mask that matches the model hierarchy, and applies it to the
provided ModelImporterClipAnimation.  
[ExtractTextures](ModelImporter.ExtractTextures.html)| Extracts the embedded
textures from a model file (such as FBX or SketchUp).  
[SearchAndRemapMaterials](ModelImporter.SearchAndRemapMaterials.html)| Search
the project for matching materials and use them instead of the internal
materials.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[GetAtPath](AssetImporter.GetAtPath.html)| Retrieves the asset importer for
the asset at path.  
---|---  
[GetImportLog](AssetImporter.GetImportLog.html)| Retrieves logs generated
during the import of the asset at path.  
[GetReferencedClipsForModelPath](ModelImporter.GetReferencedClipsForModelPath.html)|
Returns all the referenced clips matching the given model name.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
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

