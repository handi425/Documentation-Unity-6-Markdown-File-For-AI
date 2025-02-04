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

# Shader

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

[Switch to Manual](../Manual/class-Shader.html "Go to Shader Component in the
Manual")

### Description

Shader scripts used for all rendering.

Most of the advanced rendering is controlled via [Material](Material.html)
class. Shader class is mostly used just to check whether a shader can run on
the user's hardware ([isSupported](Shader-isSupported.html) property), setting
up global shader properties and keywords, and finding shaders by name
([Find](Shader.Find.html) method).  
  
Additional resources: [Material](Material.html) class,
[Materials](../Manual/Materials.html), [ShaderLab
documentation](../Manual/Shaders.html).

### Static Properties

[enabledGlobalKeywords](Shader-enabledGlobalKeywords.html)| An array
containing the global shader keywords that are currently enabled.  
---|---  
[globalKeywords](Shader-globalKeywords.html)| An array containing the global
shader keywords that currently exist. This includes enabled and disabled
global shader keywords.  
[globalMaximumLOD](Shader-globalMaximumLOD.html)| Shader LOD level for all
shaders.  
[globalRenderPipeline](Shader-globalRenderPipeline.html)| Render pipeline
currently in use.  
[maximumChunksOverride](Shader-maximumChunksOverride.html)| Sets the limit on
the number of shader variant chunks Unity loads and keeps in memory.  
  
### Properties

[isSupported](Shader-isSupported.html)| Can this shader run on the end-users
graphics card? (Read Only)  
---|---  
[keywordSpace](Shader-keywordSpace.html)| The local keyword space of this
shader.  
[maximumLOD](Shader-maximumLOD.html)| Shader LOD level for this shader.  
[passCount](Shader-passCount.html)| Returns the number of shader passes on the
active SubShader.  
[renderQueue](Shader-renderQueue.html)| Render queue of this shader. (Read
Only)  
[subshaderCount](Shader-subshaderCount.html)| Returns the number of SubShaders
in this shader.  
  
### Public Methods

[FindPassTagValue](Shader.FindPassTagValue.html)| Searches for the tag
specified by tagName on the shader's active SubShader and returns the value of
the tag.  
---|---  
[FindPropertyIndex](Shader.FindPropertyIndex.html)| Finds the index of a
shader property by its name.  
[FindSubshaderTagValue](Shader.FindSubshaderTagValue.html)| Searches for the
tag specified by tagName on the SubShader specified by subshaderIndex and
returns the value of the tag.  
[FindTextureStack](Shader.FindTextureStack.html)| Find the name of a texture
stack a texture belongs too.  
[GetDependency](Shader.GetDependency.html)| Returns the dependency shader.  
[GetPassCountInSubshader](Shader.GetPassCountInSubshader.html)| Returns the
number of passes in the given SubShader.  
[GetPropertyAttributes](Shader.GetPropertyAttributes.html)| Returns an array
of strings containing attributes of the shader property at the specified
index.  
[GetPropertyCount](Shader.GetPropertyCount.html)| Returns the number of
properties in this Shader.  
[GetPropertyDefaultFloatValue](Shader.GetPropertyDefaultFloatValue.html)|
Returns the default float value of the shader property at the specified index.  
[GetPropertyDefaultIntValue](Shader.GetPropertyDefaultIntValue.html)| Returns
the default int value of the shader property at the specified index.  
[GetPropertyDefaultVectorValue](Shader.GetPropertyDefaultVectorValue.html)|
Returns the default Vector4 value of the shader property at the specified
index.  
[GetPropertyDescription](Shader.GetPropertyDescription.html)| Returns the
description string of the shader property at the specified index.  
[GetPropertyFlags](Shader.GetPropertyFlags.html)| Returns the
ShaderPropertyFlags of the shader property at the specified index.  
[GetPropertyName](Shader.GetPropertyName.html)| Returns the name of the shader
property at the specified index.  
[GetPropertyNameId](Shader.GetPropertyNameId.html)| Returns the nameId of the
shader property at the specified index.  
[GetPropertyRangeLimits](Shader.GetPropertyRangeLimits.html)| Returns the min
and max limits for a Range property at the specified index.  
[GetPropertyTextureDefaultName](Shader.GetPropertyTextureDefaultName.html)|
Returns the default Texture name of a Texture shader property at the specified
index.  
[GetPropertyTextureDimension](Shader.GetPropertyTextureDimension.html)|
Returns the TextureDimension of a Texture shader property at the specified
index.  
[GetPropertyType](Shader.GetPropertyType.html)| Returns the ShaderPropertyType
of the property at the specified index.  
  
### Static Methods

[DisableKeyword](Shader.DisableKeyword.html)| Disables a global shader
keyword.  
---|---  
[EnableKeyword](Shader.EnableKeyword.html)| Enables a global shader keyword.  
[Find](Shader.Find.html)| Finds a shader with the given name. Returns null if
the shader is not found.  
[GetGlobalColor](Shader.GetGlobalColor.html)| Gets a global color property for
all shaders previously set using SetGlobalColor.  
[GetGlobalFloat](Shader.GetGlobalFloat.html)| Gets a global float property for
all shaders previously set using SetGlobalFloat.  
[GetGlobalFloatArray](Shader.GetGlobalFloatArray.html)| Gets a global float
array for all shaders previously set using SetGlobalFloatArray.  
[GetGlobalInt](Shader.GetGlobalInt.html)| This method is deprecated. Use
GetGlobalFloat or GetGlobalInteger instead.  
[GetGlobalInteger](Shader.GetGlobalInteger.html)| Gets a global integer
property for all shaders previously set using SetGlobalInteger.  
[GetGlobalMatrix](Shader.GetGlobalMatrix.html)| Gets a global matrix property
for all shaders previously set using SetGlobalMatrix.  
[GetGlobalMatrixArray](Shader.GetGlobalMatrixArray.html)| Gets a global matrix
array for all shaders previously set using SetGlobalMatrixArray.  
[GetGlobalTexture](Shader.GetGlobalTexture.html)| Gets a global texture
property for all shaders previously set using SetGlobalTexture.  
[GetGlobalVector](Shader.GetGlobalVector.html)| Gets a global vector property
for all shaders previously set using SetGlobalVector.  
[GetGlobalVectorArray](Shader.GetGlobalVectorArray.html)| Gets a global vector
array for all shaders previously set using SetGlobalVectorArray.  
[IsKeywordEnabled](Shader.IsKeywordEnabled.html)| Checks whether a global
shader keyword is enabled.  
[PropertyToID](Shader.PropertyToID.html)| Gets unique identifier for a shader
property name.  
[SetGlobalBuffer](Shader.SetGlobalBuffer.html)| Sets a global buffer property
for all shaders.  
[SetGlobalColor](Shader.SetGlobalColor.html)| Sets a global color property for
all shaders.  
[SetGlobalConstantBuffer](Shader.SetGlobalConstantBuffer.html)| Sets a
ComputeBuffer or GraphicsBuffer as a named constant buffer for all shader
types.  
[SetGlobalFloat](Shader.SetGlobalFloat.html)| Sets a global float property for
all shaders.  
[SetGlobalFloatArray](Shader.SetGlobalFloatArray.html)| Sets a global float
array property for all shaders.  
[SetGlobalInt](Shader.SetGlobalInt.html)| This method is deprecated. Use
SetGlobalFloat or SetGlobalInteger instead.  
[SetGlobalInteger](Shader.SetGlobalInteger.html)| Sets a global integer
property for all shaders.  
[SetGlobalMatrix](Shader.SetGlobalMatrix.html)| Sets a global matrix property
for all shaders.  
[SetGlobalMatrixArray](Shader.SetGlobalMatrixArray.html)| Sets a global matrix
array property for all shaders.  
[SetGlobalRayTracingAccelerationStructure](Shader.SetGlobalRayTracingAccelerationStructure.html)|
Sets a global RayTracingAccelerationStructure property for all shaders.  
[SetGlobalTexture](Shader.SetGlobalTexture.html)| Sets a global texture
property for all shaders.  
[SetGlobalVector](Shader.SetGlobalVector.html)| Sets a global vector property
for all shaders.  
[SetGlobalVectorArray](Shader.SetGlobalVectorArray.html)| Sets a global vector
array property for all shaders.  
[SetKeyword](Shader.SetKeyword.html)| Sets the state of a global shader
keyword.  
[WarmupAllShaders](Shader.WarmupAllShaders.html)| Prewarms all shader variants
of all Shaders currently in memory.  
  
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

