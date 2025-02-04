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

# ComputeShader

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

[Switch to Manual](../Manual/class-ComputeShader.html "Go to ComputeShader
Component in the Manual")

### Description

Compute Shader asset.

Compute shaders are programs that run on the GPU outside of the normal
rendering pipeline. They correspond to compute shader assets in the project
(.compute files).  
  
Compute shader support can be queried runtime using
[SystemInfo.supportsComputeShaders](SystemInfo-supportsComputeShaders.html).
See [Compute Shaders](../Manual/class-ComputeShader.html) overview for more
info about platforms supporting compute shaders.  
  
Additional resources: [ComputeBuffer](ComputeBuffer.html) class, [Compute
Shaders](../Manual/class-ComputeShader.html) overview.

### Properties

[enabledKeywords](ComputeShader-enabledKeywords.html)| An array containing the
local shader keywords that are currently enabled for this compute shader.  
---|---  
[keywordSpace](ComputeShader-keywordSpace.html)| The local keyword space of
this compute shader.  
[shaderKeywords](ComputeShader-shaderKeywords.html)| An array containing names
of the local shader keywords that are currently enabled for this compute
shader.  
  
### Public Methods

[DisableKeyword](ComputeShader.DisableKeyword.html)| Disables a local shader
keyword for this compute shader.  
---|---  
[Dispatch](ComputeShader.Dispatch.html)| Execute a compute shader.  
[DispatchIndirect](ComputeShader.DispatchIndirect.html)| Execute a compute
shader.  
[EnableKeyword](ComputeShader.EnableKeyword.html)| Enables a local shader
keyword for this compute shader.  
[FindKernel](ComputeShader.FindKernel.html)| Find ComputeShader kernel index.  
[GetKernelThreadGroupSizes](ComputeShader.GetKernelThreadGroupSizes.html)| Get
kernel thread group sizes.  
[HasKernel](ComputeShader.HasKernel.html)| Checks whether a shader contains a
given kernel.  
[IsKeywordEnabled](ComputeShader.IsKeywordEnabled.html)| Checks whether a
local shader keyword is enabled for this compute shader.  
[IsSupported](ComputeShader.IsSupported.html)| Allows you to check whether the
current end user device supports the features required to run the specified
compute shader kernel.  
[SetBool](ComputeShader.SetBool.html)| Set a bool parameter.  
[SetBuffer](ComputeShader.SetBuffer.html)| Sets an input or output compute
buffer.  
[SetConstantBuffer](ComputeShader.SetConstantBuffer.html)| Sets a
ComputeBuffer or GraphicsBuffer as a named constant buffer for the
ComputeShader.  
[SetFloat](ComputeShader.SetFloat.html)| Set a float parameter.  
[SetFloats](ComputeShader.SetFloats.html)| Set multiple consecutive float
parameters at once.  
[SetInt](ComputeShader.SetInt.html)| Set an integer parameter.  
[SetInts](ComputeShader.SetInts.html)| Set multiple consecutive integer
parameters at once.  
[SetKeyword](ComputeShader.SetKeyword.html)| Sets the state of a local shader
keyword for this compute shader.  
[SetMatrix](ComputeShader.SetMatrix.html)| Set a Matrix parameter.  
[SetMatrixArray](ComputeShader.SetMatrixArray.html)| Set a Matrix array
parameter.  
[SetRayTracingAccelerationStructure](ComputeShader.SetRayTracingAccelerationStructure.html)|
Sets a RayTracingAccelerationStructure to be used for Inline Ray Tracing (Ray
Queries).  
[SetTexture](ComputeShader.SetTexture.html)| Set a texture parameter.  
[SetTextureFromGlobal](ComputeShader.SetTextureFromGlobal.html)| Set a texture
parameter from a global texture property.  
[SetVector](ComputeShader.SetVector.html)| Set a vector parameter.  
[SetVectorArray](ComputeShader.SetVectorArray.html)| Set a vector array
parameter.  
  
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

