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

# RayTracingShader

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

A shader for GPU ray tracing.

This shader should contain at least a `raygeneration` shader.

### Properties

[maxRecursionDepth](Rendering.RayTracingShader-maxRecursionDepth.html)| The
maximum number of ray bounces this shader can trace (Read Only).  
---|---  
  
### Public Methods

[Dispatch](Rendering.RayTracingShader.Dispatch.html)| Dispatches this
RayTracingShader.  
---|---  
[DispatchIndirect](Rendering.RayTracingShader.DispatchIndirect.html)|
Dispatches this RayTracingShader.  
[SetAccelerationStructure](Rendering.RayTracingShader.SetAccelerationStructure.html)|
Sets the value for RayTracingAccelerationStructure property of this
RayTracingShader.  
[SetBool](Rendering.RayTracingShader.SetBool.html)| Sets the value of a
boolean uniform.  
[SetBuffer](Rendering.RayTracingShader.SetBuffer.html)| Binds an input or
output compute buffer.  
[SetConstantBuffer](Rendering.RayTracingShader.SetConstantBuffer.html)| Binds
a constant buffer created through a ComputeBuffer or a GraphicsBuffer.  
[SetFloat](Rendering.RayTracingShader.SetFloat.html)| Sets the value of a
float uniform.  
[SetFloats](Rendering.RayTracingShader.SetFloats.html)| Sets the values for a
float array uniform.  
[SetInt](Rendering.RayTracingShader.SetInt.html)| Sets the value of a int
uniform.  
[SetInts](Rendering.RayTracingShader.SetInts.html)| Sets the values for a int
array uniform.  
[SetMatrix](Rendering.RayTracingShader.SetMatrix.html)| Sets the value of a
matrix uniform.  
[SetMatrixArray](Rendering.RayTracingShader.SetMatrixArray.html)| Sets a
matrix array uniform.  
[SetShaderPass](Rendering.RayTracingShader.SetShaderPass.html)| Selects which
Shader Pass to use when executing ray/geometry intersection shaders.  
[SetTexture](Rendering.RayTracingShader.SetTexture.html)| Binds a texture
resource. This can be a input or an output texture (UAV).  
[SetTextureFromGlobal](Rendering.RayTracingShader.SetTextureFromGlobal.html)|
Binds a global texture to a RayTracingShader.  
[SetVector](Rendering.RayTracingShader.SetVector.html)| Sets the value for a
vector uniform.  
[SetVectorArray](Rendering.RayTracingShader.SetVectorArray.html)| Sets a
vector array uniform.  
  
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

