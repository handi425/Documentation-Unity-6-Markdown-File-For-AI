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

#  [Mesh](Mesh.html).CombineMeshes

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

public void CombineMeshes(CombineInstance[] combine, bool mergeSubMeshes =
true, bool useMatrices = true, bool hasLightmapData = false);

### Parameters

combine | Descriptions of the Meshes to combine.  
---|---  
mergeSubMeshes | Defines whether Meshes should be combined into a single sub-mesh.  
useMatrices | Defines whether the transforms supplied in the CombineInstance array should be used or ignored.  
hasLightmapData | Defines whether to transform the input Mesh lightmap UV data using the lightmap scale offset data in [CombineInstance](CombineInstance.html) structs.  
  
### Description

Combines several Meshes into this Mesh.

Combining Meshes is useful for performance optimization.  
  
If `mergeSubMeshes` is true, all the Meshes are combined together into a
single sub-mesh. Otherwise, each Mesh is placed in a different sub-mesh. If
all Meshes share the same Material, this property should be set to true.  
  
If `useMatrices` is true, the transform matrices in
[CombineInstance](CombineInstance.html) structs are used. Otherwise, they are
ignored.  
  
Set `hasLightmapData` to true to transform the input Mesh lightmap UV data
using the lightmap scale offset data in
[CombineInstance](CombineInstance.html) structs. The Meshes must share the
same lightmap texture.  
  
For the combined Meshes to be in the same position as the parent Mesh occupies
before the use of the method, save the parent Mesh's position and rotation
then set these values to zero before you combine the Meshes. Once the
combination is complete, set the parent Mesh's position and rotation back to
the original values.

    
    
    using UnityEngine;
    using System.Collections;  
      
    // Copy meshes from children into the parent's [Mesh](Mesh.html).
    // [CombineInstance](CombineInstance.html) stores the list of meshes.  These are combined
    // and assigned to the attached [Mesh](Mesh.html).  
      
    [[RequireComponent](RequireComponent.html)(typeof([MeshFilter](MeshFilter.html)))]
    [[RequireComponent](RequireComponent.html)(typeof([MeshRenderer](MeshRenderer.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [MeshFilter](MeshFilter.html)[] meshFilters = GetComponentsInChildren<[MeshFilter](MeshFilter.html)>();
            [CombineInstance](CombineInstance.html)[] combine = new [CombineInstance](CombineInstance.html)[meshFilters.Length];  
      
            int i = 0;
            while (i < meshFilters.Length)
            {
                combine[i].mesh = meshFilters[i].sharedMesh;
                combine[i].transform = meshFilters[i].transform.localToWorldMatrix;
                meshFilters[i].gameObject.SetActive(false);  
      
                i++;
            }  
      
            [Mesh](Mesh.html) mesh = new [Mesh](Mesh.html)();
            mesh.CombineMeshes(combine);
            transform.GetComponent<[MeshFilter](MeshFilter.html)>().sharedMesh = mesh;
            transform.gameObject.SetActive(true);
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

