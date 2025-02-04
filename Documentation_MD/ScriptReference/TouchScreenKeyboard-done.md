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

**Method group is Obsolete**  

#  [TouchScreenKeyboard](TouchScreenKeyboard.html).done

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

**Obsolete** Property done is deprecated, use status instead. public bool
done;

### Description

Specifies if input process was finished. (Read Only)

Keyboard input process can be finished either by user tapping "Done" button or
script setting `active` property to false. Note that keyboard might be
temporarily inactive (either by sliding in/out due to orientation change or by
appearance of another keyboard), however its input process might still be not
finished and will be resumed automatically.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Opens a keyboard and shows what has been typed.  
      
        [TouchScreenKeyboard](TouchScreenKeyboard.html) keyboard;
        public string text = "";  
      
        void Start()
        {
            keyboard = [TouchScreenKeyboard.Open](TouchScreenKeyboard.Open.html)(text, [TouchScreenKeyboardType.Default](TouchScreenKeyboardType.Default.html));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (keyboard != null && keyboard.status == [TouchScreenKeyboard.Status.Done](TouchScreenKeyboard.Status.Done.html))
            {
                text = keyboard.text;
                print("User input is: " + text);
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

