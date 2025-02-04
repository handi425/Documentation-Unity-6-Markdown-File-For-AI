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

#  [Screen](Screen.html).lockCursor

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

**Obsolete** Use Cursor.lockState and Cursor.visible instead. public static
bool lockCursor;

### Description

Enable cursor locking

By default, when this property is enabled, the cursor is automatically hidden,
centered on view and made to never leave the view.  
  
After the user presses escape or switches to another application the cursor
will be automatically unlocked. The cursor lock will also be lost when exiting
full screen mode. You can query if the cursor is currently locked by checking
the lockCursor state. To provide a good user experience it is recommended to
only lock the cursor as a result of pressing a button. Also you should check
if the cursor got unlocked, in order to e.g. pause the game or bring up a game
menu. In the Editor the cursor will automatically be unlocked when you press
escape. In the Standalone Player you have full control over mouse locking thus
it won't automatically lose mouse lock unless you switch applications.

    
    
    using UnityEngine;
    using UnityEngine.UI;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        [Button](UIElements.Button.html) bt;
        bool wasLocked = false;  
      
        void Start()
        {
            bt = GetComponent<[Button](UIElements.Button.html)>();
        }  
      
        // Called when the cursor is actually being locked  
      
        void DidLockCursor()
        {
            [Debug.Log](Debug.Log.html)("Locking cursor");  
      
            // Disable the button
            bt.enabled = false;
        }  
      
        // Called when the cursor is being unlocked
        // or by a script calling Screen.lockCursor = false;
        void DidUnlockCursor()
        {
            [Debug.Log](Debug.Log.html)("Unlocking cursor");  
      
            // Show the button again
            bt.enabled = true;
        }  
      
        void OnMouseDown()
        {
            // Lock the cursor
            Screen.lockCursor = true;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            // In standalone player we have to provide our own key
            // input for unlocking the cursor
            if ([Input.GetKeyDown](Input.GetKeyDown.html)("escape"))
                Screen.lockCursor = false;  
      
            // Did we lose cursor locking?
            // eg. because the user pressed escape
            // or because they switched to another application
            // or because some script set Screen.lockCursor = false;
            if (!Screen.lockCursor && wasLocked)
            {
                wasLocked = false;
                DidUnlockCursor();
            }
            // Did we gain cursor locking?
            else if (Screen.lockCursor && !wasLocked)
            {
                wasLocked = true;
                DidLockCursor();
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

