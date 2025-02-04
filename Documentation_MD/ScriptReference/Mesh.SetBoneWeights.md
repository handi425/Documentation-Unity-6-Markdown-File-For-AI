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

#  [Mesh](Mesh.html).SetBoneWeights

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

public void SetBoneWeights(NativeArray<byte> bonesPerVertex,
NativeArray<BoneWeight1> weights);

### Parameters

bonesPerVertex | Bone count for each vertex in the Mesh.  
---|---  
weights |  [BoneWeight1](BoneWeight1.html) structs for each vertex, sorted by vertex index.  
  
### Description

Sets the bone weights for the Mesh.

Supports up to 255 bone weights per vertex. The bone weights for each vertex
must be sorted with the most significant weights first. Zero weights will be
ignored.  
  
The weights may be stored with less precision than the floating point values
passed in, so do not expect to get the exact same values back using
[Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html). The minimum precision
used is currently 16-bit normalized integers.  
  
Additional resources: [Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.GetBonesPerVertex](Mesh.GetBonesPerVertex.html),
[Mesh.boneWeights](Mesh-boneWeights.html),
[Mesh.GetBoneWeights](Mesh.GetBoneWeights.html)
[ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html),
[QualitySettings.skinWeights](QualitySettings-skinWeights.html),
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html).

    
    
    using UnityEngine;
    using Unity.Collections;  
      
    public class MeshSetBoneWeights : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Animation](Animation.html) animation = gameObject.AddComponent<[Animation](Animation.html)>();
            [SkinnedMeshRenderer](SkinnedMeshRenderer.html) renderer = gameObject.AddComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();  
      
            // Build a rectangular mesh using four vertices and two triangles, and assign a material to the renderer
            [Mesh](Mesh.html) mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new [Vector3](Vector3.html)[] { new [Vector3](Vector3.html)(0, 0, 0), new [Vector3](Vector3.html)(5, 0, 0), new [Vector3](Vector3.html)(0, 5, 0), new [Vector3](Vector3.html)(5, 5, 0) };
            mesh.triangles = new int[] { 0, 1, 2, 1, 3, 2 };
            mesh.RecalculateNormals();
            renderer.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));  
      
            // Create a [Transform](Transform.html) and bind pose for two bones
            [Transform](Transform.html)[] bones = new [Transform](Transform.html)[2];
            [Matrix4x4](Matrix4x4.html)[] bindPoses = new [Matrix4x4](Matrix4x4.html)[2];  
      
            // Create a bottom-left bone as a child of this [GameObject](GameObject.html)
            bones[0] = new [GameObject](GameObject.html)("BottomLeftBone").transform;
            bones[0].parent = transform;
            bones[0].localRotation = [Quaternion.identity](Quaternion-identity.html);
            bones[0].localPosition = [Vector3.zero](Vector3-zero.html);
            // Set the bind pose to the bone's inverse transformation matrix, relative to the root
            bindPoses[0] = bones[0].worldToLocalMatrix * transform.localToWorldMatrix;  
      
            // Create a top-right bone
            bones[1] = new [GameObject](GameObject.html)("TopRightBone").transform;
            bones[1].parent = transform;
            bones[1].localRotation = [Quaternion.identity](Quaternion-identity.html);
            bones[1].localPosition = new [Vector3](Vector3.html)(5, 5, 0);
            bindPoses[1] = bones[1].worldToLocalMatrix * transform.localToWorldMatrix;  
      
            // Create an array that describes the number of bone weights per vertex
            // The array assigns 1 bone weight to vertex 0, 2 bone weights to vertex 1, and so on.
            byte[] bonesPerVertex = new byte[4] { 1, 2, 2, 1 };  
      
            // Create a array with one [BoneWeight1](BoneWeight1.html) struct for each of the 6 bone weights
            [BoneWeight1](BoneWeight1.html)[] weights = new [BoneWeight1](BoneWeight1.html)[6];  
      
            // Assign the bottom-left bone to vertex 0 (the bottom-left corner)
            weights[0].boneIndex = 0;
            weights[0].weight = 1;  
      
            // Assign both bones to vertex 1 (the bottom-right corner)
            weights[1].boneIndex = 0;
            weights[1].weight = 0.5f;  
      
            weights[2].boneIndex = 1;
            weights[2].weight = 0.5f;  
      
            // Assign both bones to vertex 2 (the top-left corner)
            weights[3].boneIndex = 0;
            weights[3].weight = 0.5f;  
      
            weights[4].boneIndex = 1;
            weights[4].weight = 0.5f;  
      
            // Assign the top-right bone to vertex 3 (the top-right corner)
            weights[5].boneIndex = 1;
            weights[5].weight = 1;  
      
            // Create NativeArray versions of the two arrays
            var bonesPerVertexArray = new NativeArray<byte>(bonesPerVertex, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var weightsArray = new NativeArray<[BoneWeight1](BoneWeight1.html)>(weights, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));  
      
            // Set the bone weights on the mesh
            mesh.SetBoneWeights(bonesPerVertexArray, weightsArray);
            bonesPerVertexArray.Dispose();
            weightsArray.Dispose();  
      
            // Assign the bind poses to the mesh
            mesh.bindposes = bindPoses;  
      
            // Assign the bones and the mesh to the renderer
            renderer.bones = bones;
            renderer.sharedMesh = mesh;  
      
            // Assign a simple back-and-forth animation to the bottom-left bone, and play the animation
            // [Vertex](UIElements.Vertex.html) 0 moves directly with the bone
            // [Vertex](UIElements.Vertex.html) 1 and 2 also move, but there's less movement because the vertices are also weighted to the top-right bone
            // [Vertex](UIElements.Vertex.html) 3 doesn't move, because the top-right bone doesn't move
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.keys = new [Keyframe](Keyframe.html)[] { new [Keyframe](Keyframe.html)(0f, 0f, 0f, 0f), new [Keyframe](Keyframe.html)(1f, 3f, 0f, 0f), new [Keyframe](Keyframe.html)(2f, 0f, 0f, 0f) };
            [AnimationClip](AnimationClip.html) clip = new [AnimationClip](AnimationClip.html)();
            clip.legacy = true;
            clip.SetCurve("BottomLeftBone", typeof([Transform](Transform.html)), "m_LocalPosition.z", curve);
            clip.wrapMode = [WrapMode.Loop](WrapMode.Loop.html);
            animation.AddClip(clip, "test");
            animation.Play("test");  
      
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

