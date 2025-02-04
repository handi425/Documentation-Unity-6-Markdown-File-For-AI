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

#  [Input](Input.html).GetKey

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

public static bool GetKey(string name);

### Description

Returns true while the user holds down the key identified by `name`.

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
[GetKey](Input.GetKey.html) will report the status of the named key. This
might be used to confirm a key is used for auto fire. For the list of key
identifiers see [Input Manager](../Manual/ConventionalGameInput.html). When
dealing with input it is recommended to use Input.GetAxis and Input.GetButton
instead since it allows end-users to configure the keys.  
  
**iOS, tvOS** : Due platform limitations, [GetKeyUp](Input.GetKeyUp.html)
event for keyboard events is delayed by about half a second, see
UnityView+Keyboard.mm in the generated Xcode project for more information.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)("up"))
            {
                print("up arrow key is held down");
            }  
      
            if ([Input.GetKey](Input.GetKey.html)("down"))
            {
                print("down arrow key is held down");
            }
        }
    }
    

* * *

## Declaration

public static bool GetKey([KeyCode](KeyCode.html) key);

### Description

Returns true while the user holds down the key identified by the `key`
[KeyCode](KeyCode.html) enum parameter.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.UpArrow](KeyCode.UpArrow.html)))
            {
                print("up arrow key is held down");
            }  
      
            if ([Input.GetKey](Input.GetKey.html)([KeyCode.DownArrow](KeyCode.DownArrow.html)))
            {
                print("down arrow key is held down");
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

