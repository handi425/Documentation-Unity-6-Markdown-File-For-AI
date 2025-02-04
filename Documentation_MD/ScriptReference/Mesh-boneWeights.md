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

#  [Mesh](Mesh.html).boneWeights

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

public BoneWeight[] boneWeights;

### Description

The [BoneWeight](BoneWeight.html) for each vertex in the Mesh, which
represents 4 bones per vertex.

The size of this array is either [Mesh.vertexCount](Mesh-vertexCount.html) or
zero. The array is sorted by vertex index.  
  
Note that this property uses [BoneWeight](BoneWeight.html) structs, which
represent exactly 4 bone weights per vertex. The newer
[BoneWeight1](BoneWeight1.html) struct describes a single bone weight, and it
can be used with the associated
[Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.SetBoneWeights](Mesh.SetBoneWeights.html) and
[Mesh.GetBonesPerVertex](Mesh.GetBonesPerVertex.html) APIs to describe up to
255 bone weights per vertex. It is preferable to use
[BoneWeight1](BoneWeight1.html) and its associated APIs; they offer more
flexibility, and might result in small performance benefits as Unity does not
have to perform unnessary conversion operations.  
  
Additional resources: [Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.SetBoneWeights](Mesh.SetBoneWeights.html),
[Mesh.GetBonesPerVertex](Mesh.GetBonesPerVertex.html),
[Mesh.GetBoneWeights](Mesh.GetBoneWeights.html),
[ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html),
[QualitySettings.skinWeights](QualitySettings-skinWeights.html),
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html).

    
    
    using UnityEngine;  
      
    public class SkinnedMeshExample : [MonoBehaviour](MonoBehaviour.html){
        void Start(){
            gameObject.AddComponent<[Animation](Animation.html)>();
            gameObject.AddComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();
            [SkinnedMeshRenderer](SkinnedMeshRenderer.html) rend = GetComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();
            [Animation](Animation.html) anim = GetComponent<[Animation](Animation.html)>();  
      
            // Build basic mesh
            [Mesh](Mesh.html) mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new [Vector3](Vector3.html)[] {new [Vector3](Vector3.html)(-1, 0, 0), new [Vector3](Vector3.html)(1, 0, 0), new [Vector3](Vector3.html)(-1, 5, 0), new [Vector3](Vector3.html)(1, 5, 0)};
            mesh.uv = new [Vector2](Vector2.html)[] {new [Vector2](Vector2.html)(0, 0), new [Vector2](Vector2.html)(1, 0), new [Vector2](Vector2.html)(0, 1), new [Vector2](Vector2.html)(1, 1)};
            mesh.triangles = new int[] { 0, 3, 1, 0, 2, 3 };
            mesh.RecalculateNormals();  
      
            // Assign mesh to mesh filter & renderer
            rend.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Diffuse"));  
      
            // Assign bone weights to mesh
            // We use 2 bones. One for the lower vertices, one for the upper vertices.
            [BoneWeight](BoneWeight.html)[] weights = new [BoneWeight](BoneWeight.html)[4];  
      
            weights[0].boneIndex0 = 0;
            weights[0].weight0 = 1;  
      
            weights[1].boneIndex0 = 0;
            weights[1].weight0 = 1;  
      
            weights[2].boneIndex0 = 1;
            weights[2].weight0 = 1;  
      
            weights[3].boneIndex0 = 1;
            weights[3].weight0 = 1;  
      
            // A BoneWeights array (weights) was just created and the boneIndex and weight assigned.
            // The weights array will now be assigned to the boneWeights array in the [Mesh](Mesh.html).
            mesh.boneWeights = weights;  
      
            // Create [Bone](XR.Bone.html) Transforms and Bind poses
            // One bone at the bottom and one at the top
            [Transform](Transform.html)[] bones = new [Transform](Transform.html)[2];
            [Matrix4x4](Matrix4x4.html)[] bindPoses = new [Matrix4x4](Matrix4x4.html)[2];  
      
            bones[0] = new [GameObject](GameObject.html)("Lower").transform;
            bones[0].parent = transform;
            // Set the position relative to the parent
            bones[0].localRotation = [Quaternion.identity](Quaternion-identity.html);
            bones[0].localPosition = [Vector3.zero](Vector3-zero.html);  
      
            // The bind pose is bone's inverse transformation matrix
            // In this case the matrix we also make this matrix relative to the root
            // So that we can move the root game object around freely
            bindPoses[0] = bones[0].worldToLocalMatrix * transform.localToWorldMatrix;  
      
            bones[1] = new [GameObject](GameObject.html)("Upper").transform;
            bones[1].parent = transform;
            // Set the position relative to the parent
            bones[1].localRotation = [Quaternion.identity](Quaternion-identity.html);
            bones[1].localPosition = new [Vector3](Vector3.html)(0, 5, 0);
            // The bind pose is bone's inverse transformation matrix
            // In this case the matrix we also make this matrix relative to the root
            // So that we can move the root game object around freely
            bindPoses[1] = bones[1].worldToLocalMatrix * transform.localToWorldMatrix;  
      
            // assign the bindPoses array to the bindposes array which is part of the mesh.
            mesh.bindposes = bindPoses;  
      
            // Assign bones and bind poses
            rend.bones = bones;
            rend.sharedMesh = mesh;  
      
            // Assign a simple waving animation to the bottom bone
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.keys = new [Keyframe](Keyframe.html)[] {new [Keyframe](Keyframe.html)(0, 0, 0, 0), new [Keyframe](Keyframe.html)(1, 3, 0, 0), new [Keyframe](Keyframe.html)(2, 0.0F, 0, 0)};  
      
            // Create the clip with the curve
            [AnimationClip](AnimationClip.html) clip = new [AnimationClip](AnimationClip.html)();
            clip.SetCurve("Lower", typeof([Transform](Transform.html)), "m_LocalPosition.z", curve);
            clip.legacy = true;
            clip.wrapMode = [WrapMode.Loop](WrapMode.Loop.html);  
      
            // Add and play the clip
            anim.AddClip(clip, "test");
            anim.Play("test");
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

