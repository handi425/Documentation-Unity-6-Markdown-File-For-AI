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

#  [TerrainData](TerrainData.html).SetDetailLayer

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

public void SetDetailLayer(int xBase, int yBase, int layer, int[,] details);

### Description

Sets the detail layer density map.

The Terrain system uses detail layer density maps. Each map is essentially a
grayscale image where each pixel value specifies the number of detail objects
to procedurally place in the terrain area that corresponds to the pixel. These
values depend on which [DetailScatterMode](DetailScatterMode.html) is set.
Because several different detail types may be used, the map is arranged into
"layers" - the array indices of the layers are determined by the order of the
detail types defined in the Terrain inspector (ie, when the Paint Details tool
is selected).

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Set all pixels in a detail map below a certain threshold to zero.
        void DetailMapCutoff([Terrain](Terrain.html) t, float threshold)
        {
            // Get all of layer zero.
            var map = t.terrainData.GetDetailLayer(0, 0, t.terrainData.detailWidth, t.terrainData.detailHeight, 0);  
      
            // For each pixel in the detail map...
            for (int y = 0; y < t.terrainData.detailHeight; y++)
            {
                for (int x = 0; x < t.terrainData.detailWidth; x++)
                {
                    // If the pixel value is below the threshold then
                    // set it to zero.
                    if (map[x, y] < threshold)
                    {
                        map[x, y] = 0;
                    }
                }
            }  
      
            // Assign the modified map back.
            t.terrainData.SetDetailLayer(0, 0, 0, map);
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

