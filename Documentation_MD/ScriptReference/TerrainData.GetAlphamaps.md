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

#  [TerrainData](TerrainData.html).GetAlphamaps

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

public float[,,] GetAlphamaps(int x, int y, int width, int height);

### Parameters

x | The x offset to read from.  
---|---  
y | The y offset to read from.  
width | The width of the alpha map area to read.  
height | The height of the alpha map area to read.  
  
### Returns

**float[,,]** A 3D array of floats, where the 3rd dimension represents the
mixing weight of each splatmap at each x,y coordinate.

### Description

Returns the alpha map at a position x, y given a width and height.

The returned array is three-dimensional - the first two dimensions represent x
and y coordinates on the map, while the third denotes the splatmap texture to
which the alphamap is applied.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // Add some random "noise" to the alphamaps.
        void AddAlphaNoise([Terrain](Terrain.html) t, float noiseScale)
        {
            float[,,] maps = t.terrainData.GetAlphamaps(0, 0, t.terrainData.alphamapWidth, t.terrainData.alphamapHeight);  
      
            for (int y = 0; y < t.terrainData.alphamapHeight; y++)
            {
                for (int x = 0; x < t.terrainData.alphamapWidth; x++)
                {
                    float a0 = maps[x, y, 0];
                    float a1 = maps[x, y, 1];  
      
                    a0 += [Random.value](Random-value.html) * noiseScale;
                    a1 += [Random.value](Random-value.html) * noiseScale;  
      
                    float total = a0 + a1;  
      
                    maps[x, y, 0] = a0 / total;
                    maps[x, y, 1] = a1 / total;
                }
            }  
      
            t.terrainData.SetAlphamaps(0, 0, maps);
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

