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

# Rect Constructor

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

public Rect(float x, float y, float width, float height);

### Parameters

x | The X value the rect is measured from.  
---|---  
y | The Y value the rect is measured from.  
width | The width of the rectangle.  
height | The height of the rectangle.  
  
### Description

Creates a new rectangle.

    
    
    using UnityEngine;  
      
    public class RectExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Rect](Rect.html) rect = new [Rect](Rect.html)(0, 0, 10, 10);  
      
            // prints: (x:0, y:0, width:10, height:10)
            [Debug.Log](Debug.Log.html)(rect);
        }
    }
    

Note: Rect represents an abstract rectangle, and can be used in a variety of
situations. As such, Rects don't have an explicit top, bottom, left or right.
For example, Y values in Camera space are measured from the bottom of the
screen, but Y values in Editor GUI space are measured from the top of the
window, therefore whether the Y value of a Rect is its "top" or "bottom" will
vary depending on where you use the Rect value. You can refer to the corners
by using [Rect.min](Rect-min.html) and [Rect.max](Rect-max.html).

* * *

## Declaration

public Rect([Vector2](Vector2.html) position, [Vector2](Vector2.html) size);

### Parameters

position | The position of the minimum corner of the rect.  
---|---  
size | The width and height of the rect.  
  
### Description

Creates a rectangle given a size and position.

This form of the constructor is convenient when you are already working with
Vector2 values.

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

