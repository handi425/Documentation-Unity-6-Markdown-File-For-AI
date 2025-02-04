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

# GraphicsSettings

class in UnityEngine.Rendering

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

[ ]()

### Description

Script interface for [Graphics Settings](../Manual/class-
GraphicsSettings.html).

### Static Properties

[allConfiguredRenderPipelines](Rendering.GraphicsSettings-
allConfiguredRenderPipelines.html)| An array containing the
RenderPipelineAsset instances that describe the default render pipeline and
any quality level overrides.  
---|---  
[cameraRelativeLightCulling](Rendering.GraphicsSettings-
cameraRelativeLightCulling.html)| Enable or disable using the camera position
as the reference point for culling lights.  
[cameraRelativeShadowCulling](Rendering.GraphicsSettings-
cameraRelativeShadowCulling.html)| Enable or disable using the camera position
as the reference point for culling shadows.  
[currentRenderPipeline](Rendering.GraphicsSettings-
currentRenderPipeline.html)| The RenderPipelineAsset that defines the active
render pipeline for the current quality level.  
[currentRenderPipelineAssetType](Rendering.GraphicsSettings-
currentRenderPipelineAssetType.html)| The type of the currently active
RenderPipelineAsset, or null if there's no currently active Asset.  
[defaultGateFitMode](Rendering.GraphicsSettings-defaultGateFitMode.html)|
Stores the default value for the GateFit property of newly created Cameras.  
[defaultRenderPipeline](Rendering.GraphicsSettings-
defaultRenderPipeline.html)| The RenderPipelineAsset that defines the default
render pipeline.  
[disableBuiltinCustomRenderTextureUpdate](Rendering.GraphicsSettings-
disableBuiltinCustomRenderTextureUpdate.html)| Disables the built-in update
loop for Custom Render Textures, so that you can write your own update loop.  
[isScriptableRenderPipelineEnabled](Rendering.GraphicsSettings-
isScriptableRenderPipelineEnabled.html)| If the value is true, a Scriptable
Render Pipeline is active.  
[lightProbeOutsideHullStrategy](Rendering.GraphicsSettings-
lightProbeOutsideHullStrategy.html)| Defines the way Unity chooses a probe to
light a Renderer that is lit by Light Probes but positioned outside the bounds
of the Light Probe tetrahedral hull.  
[lightsUseColorTemperature](Rendering.GraphicsSettings-
lightsUseColorTemperature.html)| Whether to use a Light's color temperature
when calculating the final color of that Light."  
[lightsUseLinearIntensity](Rendering.GraphicsSettings-
lightsUseLinearIntensity.html)| If this is true, Light intensity is multiplied
against linear color values. If it is false, gamma color values are used.  
[logWhenShaderIsCompiled](Rendering.GraphicsSettings-
logWhenShaderIsCompiled.html)| If this is true, a log entry is made each time
a shader is compiled at application runtime.  
[realtimeDirectRectangularAreaLights](Rendering.GraphicsSettings-
realtimeDirectRectangularAreaLights.html)| Is the current render pipeline
capable of rendering direct lighting for rectangular area Lights?  
[transparencySortAxis](Rendering.GraphicsSettings-transparencySortAxis.html)|
An axis that describes the direction along which the distances of objects are
measured for the purpose of sorting.  
[transparencySortMode](Rendering.GraphicsSettings-transparencySortMode.html)|
Transparent object sorting mode.  
[useScriptableRenderPipelineBatching](Rendering.GraphicsSettings-
useScriptableRenderPipelineBatching.html)| Enable/Disable SRP batcher
(experimental) at runtime.  
[videoShadersIncludeMode](Rendering.GraphicsSettings-
videoShadersIncludeMode.html)| If and when to include video shaders in the
build.  
  
### Static Methods

[ForEach](Rendering.GraphicsSettings.ForEach.html)| Executes the given
callback for each IRenderPipelineGraphicsSettings.  
---|---  
[GetCustomShader](Rendering.GraphicsSettings.GetCustomShader.html)| Get custom
shader used instead of a built-in shader.  
[GetGraphicsSettings](Rendering.GraphicsSettings.GetGraphicsSettings.html)|
Provides a reference to the GraphicSettings object.  
[GetRenderPipelineSettings](Rendering.GraphicsSettings.GetRenderPipelineSettings.html)|
Gets the RenderPipelineGlobalSettings asset assigned to the given
RenderPipeline asset.  
[GetSettingsForRenderPipeline](Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html)|
Get the registered RenderPipelineGlobalSettings for the given RenderPipeline.  
[GetShaderMode](Rendering.GraphicsSettings.GetShaderMode.html)| Get built-in
shader mode.  
[HasShaderDefine](Rendering.GraphicsSettings.HasShaderDefine.html)| Returns
true if shader define was set when compiling shaders for current GraphicsTier.
Graphics Tiers are only available in the Built-in Render Pipeline.  
[SetCustomShader](Rendering.GraphicsSettings.SetCustomShader.html)| Set custom
shader to use instead of a built-in shader.  
[SetShaderMode](Rendering.GraphicsSettings.SetShaderMode.html)| Set built-in
shader mode.  
[Subscribe](Rendering.GraphicsSettings.Subscribe.html)| Subscribe to changes
of properties in the IRenderPipelineGraphicsSettings.  
[TryGetCurrentRenderPipelineGlobalSettings](Rendering.GraphicsSettings.TryGetCurrentRenderPipelineGlobalSettings.html)|
Obtains the current active pipeline RenderPipelineGlobalSettings.  
[TryGetRenderPipelineSettings](Rendering.GraphicsSettings.TryGetRenderPipelineSettings.html)|
Gets a IRenderPipelineGraphicsSettings from the GraphicsSettings and returns
if the setting is found.  
[Unsubscribe](Rendering.GraphicsSettings.Unsubscribe.html)| Cancels any
subscription to changes of properties of a settings object implemented with
the IRenderPipelineGraphicsSettings interface.  
  
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

