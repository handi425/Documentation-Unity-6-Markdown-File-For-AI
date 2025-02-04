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

#  [RayTracingShader](Rendering.RayTracingShader.html).DispatchIndirect

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

## Declaration

public void DispatchIndirect(string rayGenFunctionName,
[GraphicsBuffer](GraphicsBuffer.html) argsBuffer, uint argsOffset,
[Camera](Camera.html) camera);

### Parameters

rayGenFunctionName | The name of the ray generation shader.  
---|---  
argsBuffer | Buffer containing dispatch dimensions.  
argsOffset | The byte offset into the buffer where the dispatch dimensions start.  
camera | If you pass this parameter, Unity sets up built-in shader variables related to that camera.  
  
### Description

Dispatches this [RayTracingShader](Rendering.RayTracingShader.html).

This method is similar to [Dispatch](Rendering.RayTracingShader.Dispatch.html)
but the GPU retrieves the dispatch dimensions from `argsBuffer`. The typical
use case is generating arbitrary amount of data using a
[ComputeShader](ComputeShader.html) and then dispatching that data, without
requiring a readback to the CPU to retrieve the data size.  
  
The buffer with arguments, `argsBuffer`, must contain three integer numbers at
given `argsOffset` values representing the dispatch dimensions: width, height
and depth.  
  
Additional resources: [SystemInfo.supportsIndirectDispatchRays](SystemInfo-
supportsIndirectDispatchRays.html),
[GraphicsBuffer.CopyCount](GraphicsBuffer.CopyCount.html).

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

