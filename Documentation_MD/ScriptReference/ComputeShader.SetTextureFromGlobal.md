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

#  [ComputeShader](ComputeShader.html).SetTextureFromGlobal

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

## Declaration

public void SetTextureFromGlobal(int kernelIndex, string name, string
globalTextureName);

## Declaration

public void SetTextureFromGlobal(int kernelIndex, int nameID, int
globalTextureNameID);

### Parameters

kernelIndex | For which kernel the texture is being set. See [FindKernel](ComputeShader.FindKernel.html).  
---|---  
nameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
name | Name of the buffer variable in shader code.  
globalTextureName | Global texture property to assign to shader.  
globalTextureNameID | Property name ID, use [Shader.PropertyToID](Shader.PropertyToID.html) to get it.  
  
### Description

Set a texture parameter from a global texture property.

This function can either set a regular texture that is read in the compute
shader, or an output texture that is written into by the shader. For an output
texture, it has to be a [RenderTexture](RenderTexture.html) with random write
flag enabled, see [RenderTexture.enableRandomWrite](RenderTexture-
enableRandomWrite.html).  
  
Buffers and textures are set per-kernel. Use
[FindKernel](ComputeShader.FindKernel.html) to find kernel index by function
name.  
  
Additional resources: [FindKernel](ComputeShader.FindKernel.html),
[SetBuffer](ComputeShader.SetBuffer.html),
[SetTexture](ComputeShader.SetTexture.html),
[Shader.SetGlobalTexture](Shader.SetGlobalTexture.html).

    
    
    // Assign the CameraMotionVectorsTexture global texture to a compute texture
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;  
      
    public class SampleBehaviour : [MonoBehaviour](MonoBehaviour.html)
    {
        public int renderTargetWidth;
        public int renderTargetHeight;
        [ComputeShader](ComputeShader.html) myComputeShader;  
      
        void ComputeUsingMotionVector()
        {
            int kKernelIndex = 0;  
      
            myComputeShader.SetTextureFromGlobal(kKernelIndex, "computeTexture", "_CameraMotionVectorsTexture");
            myComputeShader.Dispatch(kKernelIndex, renderTargetWidth, renderTargetHeight, 1);
        }
    }
    

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

