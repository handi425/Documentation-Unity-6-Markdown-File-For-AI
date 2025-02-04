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

# RenderPipelineAsset<T0>

class in UnityEngine.Rendering

/

Inherits
from:[Rendering.RenderPipelineAsset](Rendering.RenderPipelineAsset.html)

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

An asset that produces a specific IRenderPipeline.

Default implementation of IRenderPipelineAsset. This manages the lifecylces of
inherited types, as well as ensures that created IRenderPipeline's are
invalidated when the asset is changed.  
  
Additional resources: IRenderPipelineAsset.

### Properties

[pipelineType](Rendering.RenderPipelineAsset_1-pipelineType.html)| Returns a
RenderPipeline type associated with the given RenderPipelineAsset instance.  
---|---  
[renderPipelineShaderTag](Rendering.RenderPipelineAsset_1-renderPipelineShaderTag.html)|
Returns the Shader Tag value for the render pipeline that is described by this
asset.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
[autodeskInteractiveMaskedShader](Rendering.RenderPipelineAsset-
autodeskInteractiveMaskedShader.html)| Retrieves the default Autodesk
Interactive masked Shader for this pipeline.  
[autodeskInteractiveShader](Rendering.RenderPipelineAsset-
autodeskInteractiveShader.html)| Retrieves the default Autodesk Interactive
Shader for this pipeline.  
[autodeskInteractiveTransparentShader](Rendering.RenderPipelineAsset-
autodeskInteractiveTransparentShader.html)| Retrieves the default Autodesk
Interactive transparent Shader for this pipeline.  
[default2DMaskMaterial](Rendering.RenderPipelineAsset-
default2DMaskMaterial.html)| Gets the default 2D Mask Material used by Sprite
Masks in Universal Render Pipeline.  
[default2DMaterial](Rendering.RenderPipelineAsset-default2DMaterial.html)|
Return the default 2D Material for this pipeline.  
[defaultLineMaterial](Rendering.RenderPipelineAsset-defaultLineMaterial.html)|
Return the default Line Material for this pipeline.  
[defaultMaterial](Rendering.RenderPipelineAsset-defaultMaterial.html)| Return
the default Material for this pipeline.  
[defaultParticleMaterial](Rendering.RenderPipelineAsset-
defaultParticleMaterial.html)| Return the default particle Material for this
pipeline.  
[defaultShader](Rendering.RenderPipelineAsset-defaultShader.html)| Return the
default Shader for this pipeline.  
[defaultSpeedTree7Shader](Rendering.RenderPipelineAsset-
defaultSpeedTree7Shader.html)| Return the default SpeedTree v7 Shader for this
pipeline.  
[defaultSpeedTree8Shader](Rendering.RenderPipelineAsset-
defaultSpeedTree8Shader.html)| Return the default SpeedTree v8 Shader for this
pipeline.  
[defaultSpeedTree9Shader](Rendering.RenderPipelineAsset-
defaultSpeedTree9Shader.html)| Return the default SpeedTree v9 Shader for this
pipeline.  
[defaultTerrainMaterial](Rendering.RenderPipelineAsset-
defaultTerrainMaterial.html)| Return the default Terrain Material for this
pipeline.  
[defaultUIETC1SupportedMaterial](Rendering.RenderPipelineAsset-
defaultUIETC1SupportedMaterial.html)| Return the default UI ETC1 Material for
this pipeline.  
[defaultUIMaterial](Rendering.RenderPipelineAsset-defaultUIMaterial.html)|
Return the default UI Material for this pipeline.  
[defaultUIOverdrawMaterial](Rendering.RenderPipelineAsset-
defaultUIOverdrawMaterial.html)| Return the default UI overdraw Material for
this pipeline.  
[pipelineType](Rendering.RenderPipelineAsset-pipelineType.html)| Returns a
RenderPipeline type associated with the given RenderPipelineAsset instance.  
[renderPipelineShaderTag](Rendering.RenderPipelineAsset-
renderPipelineShaderTag.html)| Returns the Shader Tag value for the render
pipeline that is described by this asset.  
[terrainBrushPassIndex](Rendering.RenderPipelineAsset-
terrainBrushPassIndex.html)| The render index for the terrain brush in the
editor.  
[terrainDetailGrassBillboardShader](Rendering.RenderPipelineAsset-
terrainDetailGrassBillboardShader.html)| Return the detail grass billboard
Shader for this pipeline.  
[terrainDetailGrassShader](Rendering.RenderPipelineAsset-
terrainDetailGrassShader.html)| Return the detail grass Shader for this
pipeline.  
[terrainDetailLitShader](Rendering.RenderPipelineAsset-
terrainDetailLitShader.html)| Return the detail lit Shader for this pipeline.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[CreatePipeline](Rendering.RenderPipelineAsset.CreatePipeline.html)| Create a
IRenderPipeline specific to this asset.  
---|---  
[EnsureGlobalSettings](Rendering.RenderPipelineAsset.EnsureGlobalSettings.html)|
Ensures Global Settings are ready and registered into GraphicsSettings.  
[OnDisable](Rendering.RenderPipelineAsset.OnDisable.html)| Default
implementation of OnDisable for RenderPipelineAsset. See
ScriptableObject.OnDisable  
[OnValidate](Rendering.RenderPipelineAsset.OnValidate.html)| Default
implementation of OnValidate for RenderPipelineAsset. See
MonoBehaviour.OnValidate  
  
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
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

