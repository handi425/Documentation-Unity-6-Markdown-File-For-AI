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

#  [Mesh](Mesh.html).GetBonesPerVertex

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

public NativeArray<byte> GetBonesPerVertex();

### Returns

**NativeArray <byte>** Returns the number of non-zero bone weights for each
vertex.

### Description

The number of non-zero bone weights for each vertex.

The size of the returned array is either [Mesh.vertexCount](Mesh-
vertexCount.html) or zero. The array is sorted in vertex index order.  
  
Use in combination with [Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html)
to get bone weights for the vertices in the Mesh.  
  
You don't need to dispose the returned native array. However the native array
points to memory that might be deallocated or reallocated, so you should
either call `GetBonesPerVertex` every frame to get the correct data, or check
the native array is still valid each frame.  
  
Additional resources: [Mesh.GetAllBoneWeights](Mesh.GetAllBoneWeights.html),
[Mesh.SetBoneWeights](Mesh.SetBoneWeights.html),
[ModelImporter.maxBonesPerVertex](ModelImporter-maxBonesPerVertex.html),
[QualitySettings.skinWeights](QualitySettings-skinWeights.html),
[SkinnedMeshRenderer.quality](SkinnedMeshRenderer-quality.html).

    
    
    using UnityEngine;  
      
    public class TestSkinnedMesh : [MonoBehaviour](MonoBehaviour.html) {
        void Start()
        {
            // Get a reference to the mesh
            var skinnedMeshRenderer = GetComponent<[SkinnedMeshRenderer](SkinnedMeshRenderer.html)>();
            var mesh = skinnedMeshRenderer.sharedMesh;  
      
            // Get the number of bone weights per vertex
            var bonesPerVertex = mesh.GetBonesPerVertex();
            if (bonesPerVertex.Length == 0)
            {
                 return;
            }  
      
            // Get all the bone weights, in vertex index order
            var boneWeights = mesh.GetAllBoneWeights();  
      
            // Keep track of where we are in the array of BoneWeights, as we iterate over the vertices
            var boneWeightIndex = 0;  
      
            // Iterate over the vertices
            for (var vertIndex = 0; vertIndex < mesh.vertexCount; vertIndex++)
            {
                var totalWeight = 0f;
                var numberOfBonesForThisVertex = bonesPerVertex[vertIndex];
                [Debug.Log](Debug.Log.html)("This vertex has " + numberOfBonesForThisVertex + " bone influences");  
      
                // For each vertex, iterate over its BoneWeights
                for (var i = 0; i < numberOfBonesForThisVertex; i++)
                {
                    var currentBoneWeight = boneWeights[boneWeightIndex];
                    totalWeight += currentBoneWeight.weight;
                    if (i > 0)
                    {
                        [Debug.Assert](Debug.Assert.html)(boneWeights[boneWeightIndex - 1].weight >= currentBoneWeight.weight);
                    }
                    boneWeightIndex++;
                }
                [Debug.Assert](Debug.Assert.html)([Mathf.Approximately](Mathf.Approximately.html)(1f, totalWeight));
            }
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

