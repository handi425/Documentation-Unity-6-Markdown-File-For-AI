[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/net-SocialAPI.html)
  * [中文](/cn/current/Manual/net-SocialAPI.html)
  * [日本語](/ja/current/Manual/net-SocialAPI.html)
  * [한국어](/kr/current/Manual/net-SocialAPI.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/net-SocialAPI.html)
  * [中文](/cn/current/Manual/net-SocialAPI.html)
  * [日本語](/ja/current/Manual/net-SocialAPI.html)
  * [한국어](/kr/current/Manual/net-SocialAPI.html)

  * [Platform development ](PlatformSpecific.html)
  * [iOS](iphone.html)
  * [Developing for iOS](ios-developing.html)
  * Social API

[](iphone-Downloadable-Content.html)

Prepare your application for in-app purchases

[](ios-building-and-delivering.html)

Building and delivering for iOS

# Social API

**Note** : Social API is deprecated and will be removed in a future release.

Social API is Unity’s point of access to social features, such as:

  * User profiles
  * Friends lists
  * Achievements
  * Statistics / Leaderboards

It provides a unified interface to different social back-ends, such as
**GameCenter** , and is meant to be used primarily by programmers on the game
project.

The Social API is mainly an asynchronous API, and the typical way to use it is
by making a function call and registering for a callback to when that function
completes. The asynchronous function may have side effects, such as populating
certain state variables in the API, and the callback could contain data from
the server to be processed.

The Social class resides in the UnityEngine namespace and so is always
available but the other Social API classes are kept in their own namespace,
UnityEngine.SocialPlatforms. Furthermore, implementations of the Social API
are in a sub-namespace, like SocialPlatforms.GameCenter.

Here is an example of how to use the Social API:

    
    
    using UnityEngine;
    using UnityEngine.SocialPlatforms;
    
    public class SocialExample : MonoBehaviour {
    
        void Start () {
            // Authenticate and register a ProcessAuthentication callback
            // This call needs to be made before we can proceed to other calls in the Social API
            Social.localUser.Authenticate (ProcessAuthentication);
        }
    
        // This function gets called when Authenticate completes
        // Note that if the operation is successful, Social.localUser will contain data from the server.
        void ProcessAuthentication (bool success) {
            if (success) {
                Debug.Log ("Authenticated, checking achievements");
    
                // Request loaded achievements, and register a callback for processing them
                Social.LoadAchievements (ProcessLoadedAchievements);
            }
            else
                Debug.Log ("Failed to authenticate");
        }
    
        // This function gets called when the LoadAchievement call completes
        void ProcessLoadedAchievements (IAchievement[] achievements) {
            if (achievements.Length == 0)
                Debug.Log ("Error: no achievements found");
            else
                Debug.Log ("Got " + achievements.Length + " achievements");
    
            // You can also call into the functions like this
            Social.ReportProgress ("Achievement01", 100.0, result => {
                if (result)
                    Debug.Log ("Successfully reported achievement progress");
                else
                    Debug.Log ("Failed to report achievement");
            });
        }
    }
    

For more info on the Social API, see [Social API Scripting
Reference](../ScriptReference/Social.html)

[](iphone-Downloadable-Content.html)

Prepare your application for in-app purchases

[](ios-building-and-delivering.html)

Building and delivering for iOS

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

