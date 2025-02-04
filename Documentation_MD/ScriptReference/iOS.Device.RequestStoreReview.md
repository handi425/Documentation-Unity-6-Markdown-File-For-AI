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

#  [Device](iOS.Device.html).RequestStoreReview

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

public static bool RequestStoreReview();

### Returns

**bool** Value indicating whether the underlying API is available or not.
False indicates that the iOS version isn't recent enough or that the StoreKit
framework is not linked with the app.

### Description

Request App Store rating and review from the user.

Use this method to indicate when it makes sense within the user experience
flow of your application to ask the user for a review. Don't use buttons or
other controls to request feedback because the actual display of a rating
request is rate-limited and the user can opt-out of receiving these prompts.
Make sure the user has demonstrated an engagement with your application before
asking for a review. This will display the default Apple prompt that cannot be
modified.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using UnityEngine;
    using UnityEngine.iOS;  
      
    public class RequestStoreReviewExample : [MonoBehaviour](MonoBehaviour.html)
    {
        bool reviewRequested = false;  
      
        void Start()
        {
            // Note: It is advised to request AppStore review after the user interacts with your application somehow, so doing it in Start wouldn't be ideal in real scenario.
            RequestReview();
        }  
      
        void RequestReview()
        {
            if (reviewRequested == false)
            {
                bool popupShown = [Device.RequestStoreReview](iOS.Device.RequestStoreReview.html)();
                if (popupShown)
                {
                    // The review popup was presented to the user, set "reviewRequested" to "true" to reflect that
                    // Note: there's no way to check if the user actually gave a review for the app or cancelled the popup.
                    reviewRequested = true;
                }
                else
                {
                    // The review popup wasn't presented. Log a message and reset "reviewRequested" so you can revisit this in the future.
                    [Debug.Log](Debug.Log.html)("[iOS](PlayerSettings.iOS.html) version is too low or StoreKit framework was not linked.");
                    reviewRequested = false;
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

