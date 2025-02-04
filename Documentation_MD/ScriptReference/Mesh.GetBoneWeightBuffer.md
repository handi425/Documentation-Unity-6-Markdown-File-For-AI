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

#  [Mesh](Mesh.html).GetBoneWeightBuffer

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

## Declaration

public [GraphicsBuffer](GraphicsBuffer.html)
GetBoneWeightBuffer([SkinWeights](SkinWeights.html) layout);

### Parameters

layout | Which buffer to access, based on maximum bones per vertex.  
---|---  
  
### Returns

**GraphicsBuffer** The bone weight data as a
[GraphicsBuffer](GraphicsBuffer.html).

### Description

Retrieves a [GraphicsBuffer](GraphicsBuffer.html) that provides direct read
and write access to GPU bone weight data.

The buffer that this function returns is called the bone weight buffer. It
contains indices and weights to use for skinning.  
  
To know which buffer the mesh is using, call [skinWeightBufferLayout](Mesh-
skinWeightBufferLayout.html).  
  
It is possible to access the buffer with a lower SkinWeigts setting, for
instance a mesh with [SkinWeights.Unlimited](SkinWeights.Unlimited.html) can
be accessed with [SkinWeights.FourBones](SkinWeights.FourBones.html) and
[SkinWeights.TwoBones](SkinWeights.TwoBones.html). However, a mesh with
[SkinWeights.FourBones](SkinWeights.FourBones.html) can not be accessed using
[SkinWeights.Unlimited](SkinWeights.Unlimited.html).  
  
[Mesh.isReadable](Mesh-isReadable.html) does not need to be `true` to access
this data.  
  
After using this buffer, you should dispose of it.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Mesh](Mesh.html) mesh;
        public [ComputeShader](ComputeShader.html) computeShader;  
      
        void Start()
        {
            // Fetch [GraphicsBuffer](GraphicsBuffer.html) with [Bone](XR.Bone.html) Weight data
            var boneWeightBuffer = mesh.GetBoneWeightBuffer(mesh.skinWeightBufferLayout);  
      
            // Set [Bone](XR.Bone.html) Weight data to a compute shader
            computeShader.SetBuffer(0, "BoneWeightBuffer", boneWeightBuffer);  
      
            // Dispatch compute shader and access [Bone](XR.Bone.html) Weight data on the GPU
            computeShader.Dispatch(0, 64, 1, 1);  
      
            // Dispose of [GraphicsBuffer](GraphicsBuffer.html) to avoid leaking memory
            boneWeightBuffer .Dispose();
        }  
      
    }
    

Additional resources: Mesh.skinWeightsBufferLayout,
[Mesh.GetBlendShapeBuffer](Mesh.GetBlendShapeBuffer.html)

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

