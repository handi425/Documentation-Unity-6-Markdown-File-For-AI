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

# ScrollViewScope

class in UnityEngine

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

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

### Description

Disposable helper class for managing
[BeginScrollView](GUI.BeginScrollView.html) /
[EndScrollView](GUI.EndScrollView.html).

[BeginScrollView](GUI.BeginScrollView.html) is called at construction, and
[EndScrollView](GUI.EndScrollView.html) is called when the instance is
disposed. ScrollViews let you make a smaller area on-screen look 'into' a much
larger area, using scrollbars placed on the sides of the ScrollView.

    
    
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        // The position of the scrolling viewport
        public [Vector2](Vector2.html) scrollPosition = [Vector2.zero](Vector2-zero.html);
        void OnGUI()
        {
            // An absolute-positioned example: We make a scrollview that has a really large client
            // rect and put it in a small rect on the screen.
            using (var scrollScope = new [GUI.ScrollViewScope](GUI.ScrollViewScope.html)(new [Rect](Rect.html)(10, 300, 100, 100), scrollPosition, new [Rect](Rect.html)(0, 0, 220, 200)))
            {
                scrollPosition = scrollScope.scrollPosition;  
      
                // Make four buttons - one in each corner. The coordinate system is defined
                // by the last parameter to the ScrollScope constructor.
                [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 0, 100, 20), "Top-left");
                [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(120, 0, 100, 20), "Top-right");
                [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(0, 180, 100, 20), "Bottom-left");
                [GUI.Button](GUI.Button.html)(new [Rect](Rect.html)(120, 180, 100, 20), "Bottom-right");
            }
            // Now the scroll view is ended.
        }
    }
    

### Properties

[handleScrollWheel](GUI.ScrollViewScope-handleScrollWheel.html)| Whether this
ScrollView should handle scroll wheel events. (default: true).  
---|---  
[scrollPosition](GUI.ScrollViewScope-scrollPosition.html)| The modified
scrollPosition. Feed this back into the variable you pass in, as shown in the
example.  
  
### Constructors

[GUI.ScrollViewScope](GUI.ScrollViewScope-ctor.html)| Create a new
ScrollViewScope and begin the corresponding ScrollView.  
---|---  
  
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

