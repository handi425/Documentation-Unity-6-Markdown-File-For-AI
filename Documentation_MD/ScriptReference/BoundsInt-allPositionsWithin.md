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

#  [BoundsInt](BoundsInt.html).allPositionsWithin

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

public [BoundsInt.PositionEnumerator](BoundsInt.PositionEnumerator.html)
allPositionsWithin;

### Description

A BoundsInt.PositionCollection that contains all positions within the
[BoundsInt](BoundsInt.html).

Positions within the BoundsInt are not inclusive of the positions on the upper
limits of the BoundsInt. This iterator will only return positions of size
greater than zero for each axis.

    
    
    using UnityEngine;  
      
    public class ExampleScript : [MonoBehaviour](MonoBehaviour.html)
    {
        // Create a [BoundsInt](BoundsInt.html) of a cube with a
        // bottom-left coordinate of (0, 0, 0),
        // and a height, width and depth of 4,
        // and log its contained points to the console.
        void Start()
        {
            // bounds is a cube where every edge has exactly four points.
            // It has 4 * 4 * 4 = 64 points.
            // min = (0,0,0), max = (3,3,3).
            var bounds = new [BoundsInt](BoundsInt.html)(new [Vector3Int](Vector3Int.html)(0, 0, 0), new [Vector3Int](Vector3Int.html)(4, 4, 4));  
      
            // Iterate through each point, and log it to the [Debug](Debug.html) Console.
            foreach (var point in bounds.allPositionsWithin)
            {
                [Debug.Log](Debug.Log.html)(point.ToString());
            }  
      
            // The 64 unique integer 3-dimensional points that fall within this [Bounds](Bounds.html) will be logged to the [Debug](Debug.html) Console.
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

