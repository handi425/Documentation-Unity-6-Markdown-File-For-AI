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

# ShaderUtil

class in UnityEditor

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

Utility functions to assist with working with shaders from the editor.

### Static Properties

[allowAsyncCompilation](ShaderUtil-allowAsyncCompilation.html)| When true,
asynchronous Shader compilation is allowed at the current call site.  
---|---  
[anythingCompiling](ShaderUtil-anythingCompiling.html)| When true, the Editor
is compiling some Shaders asynchronously at the point of query.  
[disableShaderOptimization](ShaderUtil-disableShaderOptimization.html)|
Disables shader optimization in the Editor.  
[hardwareSupportsRectRenderTexture](ShaderUtil-
hardwareSupportsRectRenderTexture.html)| Does the current hardware support
render textues.  
  
### Static Methods

[ClearCachedData](ShaderUtil.ClearCachedData.html)| Clears all internally-
cached data that was generated for the given shader, such as errors and
compilation info.  
---|---  
[ClearShaderMessages](ShaderUtil.ClearShaderMessages.html)| Clear compile time
messages for the given shader.  
[CompilePass](ShaderUtil.CompilePass.html)| Request the Editor to compile the
Shader Variant needed for the specific pass of the given Material.  
[CreateComputeShaderAsset](ShaderUtil.CreateComputeShaderAsset.html)| Creates
a new ComputeShader object from the provided source code string. You can use
this method alongside the ScriptedImporter to create custom compute shader
generation tools in the Editor.  
[CreateRayTracingShaderAsset](ShaderUtil.CreateRayTracingShaderAsset.html)|
Creates a new RayTracingShader object from the provided source code string.
You can use this method alongside the ScriptedImporter to create custom ray
tracing shader generation tools in the Editor.  
[CreateShaderAsset](ShaderUtil.CreateShaderAsset.html)| Creates a new Shader
object from the provided source code string. You can use this method alongside
the ScriptedImporter to create custom shader generation tools in the Editor.  
[GetAllShaderInfo](ShaderUtil.GetAllShaderInfo.html)| Returns an array of
ShaderInfo of all available shaders. That includes built-in shaders.  
[GetCallableShaderCount](ShaderUtil.GetCallableShaderCount.html)| Returns the
number of callable Shaders defined whitin a given RayTracingShader.  
[GetCallableShaderName](ShaderUtil.GetCallableShaderName.html)| Returns the
name of a user-defined callable Shader from within a RayTracingShader.  
[GetCallableShaderParamSize](ShaderUtil.GetCallableShaderParamSize.html)|
Returns the parameter size of a user-defined callable Shader from within a
RayTracingShader.  
[GetComputeShaderMessageCount](ShaderUtil.GetComputeShaderMessageCount.html)|
Returns the number of errors and warnings generated by the Unity Shader
Compiler for the given ComputeShader.  
[GetComputeShaderMessages](ShaderUtil.GetComputeShaderMessages.html)| Returns
each error and warning generated by the Unity Shader Compiler for the given
ComputeShader.  
[GetCurrentCustomEditor](ShaderUtil.GetCurrentCustomEditor.html)| Gets the
current custom editor for the shader you pass in.Depending on the render
pipeline asset assigned in your Graphics Settings, the custom editor can
change if the shader has a different custom editor for one or multiple render
pipeline assets.  
[GetCustomEditorForRenderPipeline](ShaderUtil.GetCustomEditorForRenderPipeline.html)|
Gets the shader's custom editor class name for a specific render pipeline
asset type.  
[GetMissShaderCount](ShaderUtil.GetMissShaderCount.html)| Returns the number
of miss Shaders defined whitin a given RayTracingShader.  
[GetMissShaderName](ShaderUtil.GetMissShaderName.html)| Returns the name of a
user-defined miss Shader from within a RayTracingShader.  
[GetMissShaderRayPayloadSize](ShaderUtil.GetMissShaderRayPayloadSize.html)|
Returns the ray payload size of a user-defined miss Shader from within a
RayTracingShader.  
[GetPassKeywords](ShaderUtil.GetPassKeywords.html)| Gets the local shader
keywords that are valid for a Pass within a particular shader.  
[GetPropertyCount](ShaderUtil.GetPropertyCount.html)| Get the number of
properties in Shader s.  
[GetPropertyDescription](ShaderUtil.GetPropertyDescription.html)| Get the
description of the shader propery at index propertyIdx of Shader s.  
[GetPropertyName](ShaderUtil.GetPropertyName.html)| Get the name of the shader
propery at index propertyIdx of Shader s.  
[GetPropertyType](ShaderUtil.GetPropertyType.html)| Get the ShaderProperyType
of the shader propery at index propertyIdx of Shader s.  
[GetRangeLimits](ShaderUtil.GetRangeLimits.html)| Get Limits for a range
property at index propertyIdx of Shader s.  
[GetRayGenerationShaderCount](ShaderUtil.GetRayGenerationShaderCount.html)|
Returns the number of ray generation Shaders defined whitin a given
RayTracingShader.  
[GetRayGenerationShaderName](ShaderUtil.GetRayGenerationShaderName.html)|
Returns the name of a user-defined ray generation Shader from within a
RayTracingShader.  
[GetRayTracingShaderMessageCount](ShaderUtil.GetRayTracingShaderMessageCount.html)|
Returns the number of errors and warnings generated by the Shader Compiler for
the given RayTracingShader.  
[GetRayTracingShaderMessages](ShaderUtil.GetRayTracingShaderMessages.html)|
Returns each error and warning generated by the Shader Compiler for the given
RayTracingShader.  
[GetShaderData](ShaderUtil.GetShaderData.html)| Get the shader data for a
specific shader.  
[GetShaderInfo](ShaderUtil.GetShaderInfo.html)| Gets ShaderInfo for the given
shader.  
[GetShaderMessageCount](ShaderUtil.GetShaderMessageCount.html)| Returns the
number of errors and warnings generated by the Unity Shader Compiler for the
given Shader.  
[GetShaderMessages](ShaderUtil.GetShaderMessages.html)| Returns each error and
warning generated by the Unity Shader Compiler for the given Shader.  
[GetShaderPlatformKeywordsForBuildTarget](ShaderUtil.GetShaderPlatformKeywordsForBuildTarget.html)|
Gets the platform keywords for a shader, given a shader compiler platform,
build target, and optional graphics tier. These platform keywords are
necessary to properly compile a shader for a given target.  
[GetTexDim](ShaderUtil.GetTexDim.html)| Gets texture dimension of a shader
property.  
[HasProceduralInstancing](ShaderUtil.HasProceduralInstancing.html)| Determines
whether the specified Shader contains a valid Procedural Instancing variant.  
[IsPassCompiled](ShaderUtil.IsPassCompiled.html)| Checks if the Shader variant
for the given pass in the Material has already been compiled.  
[IsShaderPropertyHidden](ShaderUtil.IsShaderPropertyHidden.html)| Returns true
if the shader propery at index propertyIdx is hidden with the
[HideInInspector] attribute in the shader code.  
[IsShaderPropertyNonModifiableTexureProperty](ShaderUtil.IsShaderPropertyNonModifiableTexureProperty.html)|
Is the shader propery at index propertyIdx of Shader s a
NonModifiableTextureProperty?  
[PassHasKeyword](ShaderUtil.PassHasKeyword.html)| Checks whether a local
shader keyword is valid for a Pass within a particular shader.  
[RegisterShader](ShaderUtil.RegisterShader.html)| Register a user created
shader.  
[RestoreAsyncCompilation](ShaderUtil.RestoreAsyncCompilation.html)| Restores
the previous Shader compilation mode in this CommandBuffer scope.  
[SetAsyncCompilation](ShaderUtil.SetAsyncCompilation.html)| Adds shader
compilation mode command in the CommandBuffer.  
[ShaderHasError](ShaderUtil.ShaderHasError.html)| Checks if a shader has any
compilation errors. Ignores warnings.  
[ShaderHasWarnings](ShaderUtil.ShaderHasWarnings.html)| Checks if a shader has
any compilation warnings. Ignores errors.  
[UpdateShaderAsset](ShaderUtil.UpdateShaderAsset.html)| Replaces the existing
source code in the specified shader with the source code in the supplied
string.  
  
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

