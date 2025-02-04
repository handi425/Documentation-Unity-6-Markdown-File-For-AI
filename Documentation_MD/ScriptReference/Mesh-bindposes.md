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

#  [Mesh](Mesh.html).bindposes

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

public Matrix4x4[] bindposes;

### Description

The bind poses. The bind pose at each index refers to the bone with the same
index.

Each matrix in `bindposes` is the inverse of the transformation matrix of the
bone, calculated when the bone is in its base state (its bind pose).  
  
**Note:** See the [Mesh](Mesh.html) page where example 2 shows vertices being
copied, updated and and re-assigned to the [Mesh](Mesh.html). The example on
this page also updates [bindposes](Mesh-bindposes.html),
[SkinnedMeshRenderer.bones](SkinnedMeshRenderer-bones.html) and
[SkinnedMeshRenderer.sharedMesh](SkinnedMeshRenderer-sharedMesh.html) in the
same way.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // this example creates a quad mesh from scratch, creates bones
    // and assigns them, and animates the bones motion to make the
    // quad animate based on a simple animation curve.
    public class BindPoseExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            gameObject.AddComponent<[Animation](Animation.html)>();
            gameObject.AddComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();
            [SkinnedMeshRenderer](SkinnedMeshRenderer.html) rend = GetComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();
            [Animation](Animation.html) anim = GetComponent<[Animation](Animation.html)>();  
      
            // Build basic mesh
            [Mesh](Mesh.html) mesh = new [Mesh](Mesh.html)();
            mesh.vertices = new [Vector3](Vector3.html)[] { new [Vector3](Vector3.html)(-1, 0, 0), new [Vector3](Vector3.html)(1, 0, 0), new [Vector3](Vector3.html)(-1, 5, 0), new [Vector3](Vector3.html)(1, 5, 0) };
            mesh.uv = new [Vector2](Vector2.html)[] { new [Vector2](Vector2.html)(0, 0), new [Vector2](Vector2.html)(1, 0), new [Vector2](Vector2.html)(0, 1), new [Vector2](Vector2.html)(1, 1) };
            mesh.triangles = new int[] { 2, 3, 1, 2, 1, 0 };
            mesh.RecalculateNormals();
            rend.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Diffuse"));  
      
            // assign bone weights to mesh
            [BoneWeight](BoneWeight.html)[] weights = new [BoneWeight](BoneWeight.html)[4];
            weights[0].boneIndex0 = 0;
            weights[0].weight0 = 1;
            weights[1].boneIndex0 = 0;
            weights[1].weight0 = 1;
            weights[2].boneIndex0 = 1;
            weights[2].weight0 = 1;
            weights[3].boneIndex0 = 1;
            weights[3].weight0 = 1;
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
      
            // bindPoses was created earlier and was updated with the required matrix.
            // The bindPoses array will now be assigned to the bindposes in the [Mesh](Mesh.html).
            mesh.bindposes = bindPoses;  
      
            // Assign bones and bind poses
            rend.bones = bones;
            rend.sharedMesh = mesh;  
      
            // Assign a simple waving animation to the bottom bone
            [AnimationCurve](AnimationCurve.html) curve = new [AnimationCurve](AnimationCurve.html)();
            curve.keys = new [Keyframe](Keyframe.html)[] { new [Keyframe](Keyframe.html)(0, 0, 0, 0), new [Keyframe](Keyframe.html)(1, 3, 0, 0), new [Keyframe](Keyframe.html)(2, 0.0F, 0, 0) };  
      
            // Create the clip with the curve
            [AnimationClip](AnimationClip.html) clip = new [AnimationClip](AnimationClip.html)();
            clip.legacy = true;
            clip.SetCurve("Lower", typeof([Transform](Transform.html)), "m_LocalPosition.z", curve);  
      
            // Add and play the clip
            clip.wrapMode = [WrapMode.Loop](WrapMode.Loop.html);
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

