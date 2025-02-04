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

#  [ILocalUser](SocialPlatforms.ILocalUser.html).Authenticate

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

**Obsolete** ILocalUser is deprecated and will be removed in a future release.

## Declaration

public void Authenticate(Action<bool> callback);

**Obsolete** ILocalUser is deprecated and will be removed in a future release.

## Declaration

public void Authenticate(Action<bool,string> callback);

### Parameters

callback | Callback that is called whenever the authentication operation is finished. The first parameter is a Boolean identifying whether the authentication operation was successful. The optional second argument contains a string identifying any errors (if available) if the operation was unsuccessful.  
---|---  
  
### Description

Authenticate the local user to the current active Social API implementation
and fetch his profile data.

This should be done before any other calls into the API. Depending on the
platform, this might trigger a potentially blocking dialog for providing login
details.  
  
On certain platforms (including but not limited to iOS and tvOS), the callback
is only invoked on the first call to Authenticate(). Subsequent calls to
Authenticate() on such platforms results in no callback being triggered. This
can occur if, for example, the user or the OS cancels the authentication
operation before it has completed. Please ensure you test for this situation.

    
    
    using UnityEngine;
    using UnityEngine.SocialPlatforms;
    using System.Collections;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            Social.localUser.Authenticate(success => {
                if (success)
                {
                    [Debug.Log](Debug.Log.html)("Authentication successful");
                    string userInfo = "Username: " + Social.localUser.userName +
                        "\nUser ID: " + Social.localUser.id +
                        "\nIsUnderage: " + Social.localUser.underage;
                    [Debug.Log](Debug.Log.html)(userInfo);
                }
                else
                    [Debug.Log](Debug.Log.html)("Authentication failed");
            });
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

