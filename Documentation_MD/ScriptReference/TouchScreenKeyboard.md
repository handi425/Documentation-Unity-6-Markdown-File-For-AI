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

# TouchScreenKeyboard

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Interface for on-screen keyboards. Only native iPhone, Android, and Windows
Store Apps are supported.

This interface allows to display different types of the keyboard: ASCII,
Numbers, URL, Email, and others.  
  
Because the appearance of the keyboard has the potential to obscure portions
of your user interface, it is up to you to make sure that parts of your user
interface are not obscured when the keyboard is being displayed.  
  
`TouchScreenKeyboard.visible` and `TouchScreenKeyboard.area` should be used to
determine if the keyboard is being shown (activated) and what portion of the
screen is using.  
  
**Universal Windows Platform** : On Universal Windows Apps the touch screen
keyboard is supported when physical keyboard is not connected.

### Static Properties

[area](TouchScreenKeyboard-area.html)| Returns portion of the screen which is
covered by the keyboard.  
---|---  
[hideInput](TouchScreenKeyboard-hideInput.html)| Will text input field above
the keyboard be hidden when the keyboard is on screen?  
[inputFieldAppearance](TouchScreenKeyboard-inputFieldAppearance.html)| Returns
the status of the on-screen keyboard's input field.  
[isInPlaceEditingAllowed](TouchScreenKeyboard-isInPlaceEditingAllowed.html)|
Checks if the text within an input field can be selected and modified while
TouchScreenKeyboard is open.  
[isSupported](TouchScreenKeyboard-isSupported.html)| Is touch screen keyboard
supported.  
[visible](TouchScreenKeyboard-visible.html)| Returns true whenever any
keyboard is visible on the screen.  
  
### Properties

[active](TouchScreenKeyboard-active.html)| Is the keyboard visible or sliding
into the position on the screen?  
---|---  
[canGetSelection](TouchScreenKeyboard-canGetSelection.html)| Specifies whether
the TouchScreenKeyboard supports the selection property. (Read Only)  
[canSetSelection](TouchScreenKeyboard-canSetSelection.html)| Specifies whether
the TouchScreenKeyboard supports the selection property. (Read Only)  
[characterLimit](TouchScreenKeyboard-characterLimit.html)| How many characters
the keyboard input field is limited to. 0 = infinite.  
[selection](TouchScreenKeyboard-selection.html)| Gets or sets the character
range of the selected text within the string currently being edited.  
[status](TouchScreenKeyboard-status.html)| Returns the status of the on-screen
keyboard. (Read Only)  
[targetDisplay](TouchScreenKeyboard-targetDisplay.html)| Specified on which
display the on-screen keyboard will appear.  
[text](TouchScreenKeyboard-text.html)| Returns the text displayed by the input
field of the keyboard.  
[type](TouchScreenKeyboard-type.html)| Returns the TouchScreenKeyboardType of
the keyboard.  
  
### Static Methods

[Open](TouchScreenKeyboard.Open.html)| Opens the native keyboard provided by
OS on the screen.  
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

