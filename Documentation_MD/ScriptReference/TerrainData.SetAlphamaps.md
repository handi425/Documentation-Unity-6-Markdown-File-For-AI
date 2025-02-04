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

#  [TerrainData](TerrainData.html).SetAlphamaps

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

public void SetAlphamaps(int x, int y, float[,,] map);

### Description

Assign all splat values in the given map area.

The array supplied to this function determines the width and height of the
portion to be replaced. The third dimension of the array corresponds to the
number of splatmap textures.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Terrain](Terrain.html) t;
        // Blend the two terrain textures according to the steepness of
        // the slope at each point.
        void Start()
        {
            float[,,] map = new float[t.terrainData.alphamapWidth, t.terrainData.alphamapHeight, 2];  
      
            // For each point on the alphamap...
            for (int y = 0; y < t.terrainData.alphamapHeight; y++)
            {
                for (int x = 0; x < t.terrainData.alphamapWidth; x++)
                {
                    // Get the normalized terrain coordinate that
                    // corresponds to the point.
                    float normX = x * 1.0f / (t.terrainData.alphamapWidth - 1);
                    float normY = y * 1.0f / (t.terrainData.alphamapHeight - 1);  
      
                    // Get the steepness value at the normalized coordinate.
                    var angle = t.terrainData.GetSteepness(normX, normY);  
      
                    // Steepness is given as an angle, 0..90 degrees. Divide
                    // by 90 to get an alpha blending value in the range 0..1.
                    var frac = angle / 90.0;
                    map[x, y, 0] = (float)frac;
                    map[x, y, 1] = (float)(1 - frac);
                }
            }
            t.terrainData.SetAlphamaps(0, 0, map);
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

