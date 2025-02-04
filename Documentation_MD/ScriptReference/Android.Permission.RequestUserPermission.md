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

#  [Permission](Android.Permission.html).RequestUserPermission

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

public static void RequestUserPermission(string permission);

## Declaration

public static void RequestUserPermission(string permission,
[Android.PermissionCallbacks](Android.PermissionCallbacks.html) callbacks);

### Parameters

permission | A string that describes the permission to request. For permissions which Unity has not predefined, you can provide Android's in-built permission strings such as "android.permission.READ_CONTACTS". For a list of permission strings, refer to Android's documentation on [ Manifest.permission](https://developer.android.com/reference/android/Manifest.permission).  
---|---  
callbacks | An instance of callbacks invoked when permission request is executed.  
  
### Description

Request the user to grant access to a device resource or information that
requires authorization.

    
    
    using UnityEngine;
    using UnityEngine.Android;  
      
    public class RequestPermissionScript : [MonoBehaviour](MonoBehaviour.html)
    {
        internal void PermissionCallbacks_PermissionDeniedAndDontAskAgain(string permissionName)
        {
            [Debug.Log](Debug.Log.html)($"{permissionName} PermissionDeniedAndDontAskAgain");
        }  
      
        internal void PermissionCallbacks_PermissionGranted(string permissionName)
        {
            [Debug.Log](Debug.Log.html)($"{permissionName} PermissionCallbacks_PermissionGranted");
        }  
      
        internal void PermissionCallbacks_PermissionDenied(string permissionName)
        {
            [Debug.Log](Debug.Log.html)($"{permissionName} PermissionCallbacks_PermissionDenied");
        }  
      
        void Start()
        {
            if ([Permission.HasUserAuthorizedPermission](Android.Permission.HasUserAuthorizedPermission.html)([Permission.Microphone](Android.Permission.Microphone.html)))
            {
                // The user authorized use of the microphone.
            }
            else
            {
                bool useCallbacks = false;
                if (!useCallbacks)
                {
                    // We do not have permission to use the microphone.
                    // Ask for permission or proceed without the functionality enabled.
                    [Permission.RequestUserPermission](Android.Permission.RequestUserPermission.html)([Permission.Microphone](Android.Permission.Microphone.html));
                }
                else
                {
                    var callbacks = new [PermissionCallbacks](Android.PermissionCallbacks.html)();
                    callbacks.PermissionDenied += PermissionCallbacks_PermissionDenied;
                    callbacks.PermissionGranted += PermissionCallbacks_PermissionGranted;
                    callbacks.PermissionDeniedAndDontAskAgain += PermissionCallbacks_PermissionDeniedAndDontAskAgain;
                    [Permission.RequestUserPermission](Android.Permission.RequestUserPermission.html)([Permission.Microphone](Android.Permission.Microphone.html), callbacks);
                }
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

