[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/deep-linking.html)
  * [中文](/cn/current/Manual/deep-linking.html)
  * [日本語](/ja/current/Manual/deep-linking.html)
  * [한국어](/kr/current/Manual/deep-linking.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/deep-linking.html)
  * [中文](/cn/current/Manual/deep-linking.html)
  * [日本語](/ja/current/Manual/deep-linking.html)
  * [한국어](/kr/current/Manual/deep-linking.html)

  * [Platform development ](PlatformSpecific.html)
  * [Cross-platform features and considerations](cross-platform-features.html)
  * Deep linking

[](UnityasaLibrary.html)

Using Unity as a Library in other applications

[](XcodeFrameDebuggerIntegration.html)

Xcode frame debugger Unity integration

# Deep linking

Deep links are hyperlinks that take a user to a specific location within an
application rather than a website. When a user selects a deep link, the
application opens at the designated location, such as a specific **scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in a Unity application. Unity uses the
[Application.absoluteURL](../ScriptReference/Application-absoluteURL.html)
property and [Application.deepLinkActivated](../ScriptReference/Application-
deepLinkActivated.html) event to support deep linking.

## Enable deep linking

Before you can process deep links, you need to configure your application to
react to them. The process to configure an application to react to specific
URLs is platform-specific. Unity supports deep links for the following
platforms:

  * [iOS](deep-linking-ios.html)
  * [Android](deep-linking-android.html)
  * [Universal Windows Platform](deep-linking-universal-windows-platform.html)
  * [macOS](deep-linking-macos.html)

## Use deep links

There are two ways to process a deep link that depend on the current state of
the application:

  * The application isn’t running: The device opens the application and [Application.absoluteURL](../ScriptReference/Application-absoluteURL.html) stores the deep link URL that the device passes to the application.
  * The application is running: The device passes the URL to the application and calls the [Application.deepLinkActivated](../ScriptReference/Application-deepLinkActivated.html) event using the deep link URL as a parameter. [Application.absoluteURL](../ScriptReference/Application-absoluteURL.html) updates at the same time.

In both cases, use [Application.absoluteURL](../ScriptReference/Application-
absoluteURL.html) to select the scene to open in the application.

The following code sample shows you how to process a deep link depending on
the current state of the application:

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;
    
    public class ProcessDeepLinkMngr : MonoBehaviour
    {
        public static ProcessDeepLinkMngr Instance { get; private set; }
        public string deeplinkURL;
        private void Awake()
        {
            if (Instance == null)
            {
                Instance = this;                
                Application.deepLinkActivated += onDeepLinkActivated;
                if (!string.IsNullOrEmpty(Application.absoluteURL))
                {
                    // Cold start and Application.absoluteURL not null so process Deep Link.
                    onDeepLinkActivated(Application.absoluteURL);
                }
                // Initialize DeepLink Manager global variable.
                else deeplinkURL = "[none]";
                DontDestroyOnLoad(gameObject);
            }
            else
            {
                Destroy(gameObject);
            }
        }
     
        private void onDeepLinkActivated(string url)
        {
            // Update DeepLink Manager global variable, so URL can be accessed from anywhere.
            deeplinkURL = url;
            
    // Decode the URL to determine action. 
    // In this example, the application expects a link formatted like this:
    // unitydl://mylink?scene1
            string sceneName = url.Split('?')[1];
            bool validScene;
            switch (sceneName)
            {
                case "scene1":
                    validScene = true;
                    break;
                case "scene2":
                    validScene = true;
                    break;
                default:
                    validScene = false;
                    break;
            }
            if (validScene) SceneManager.LoadScene(sceneName);
        }
    }
    

## Test a deep link

To test a deep link, use the following steps:

  1. Create a HTML file that includes the deep link to test.
  2. Host the HTML file on a local web server.
  3. Open the HTML file from a web browser on your device and click the deep link.

### Example HTML file

This is an example HTML file that you can use to test deep links. To redirect
the link, change the `href` attribute in one of the `<a>` elements.

    
    
    <html>
        <head>
           <meta charset="utf-8">
        </head>
        <body >
           <h1>My Deep Link Test page</h1>
           <p><a href="unitydl://mylink">Launch</a></p>
           <p><a href="unitydl://mylink?parameter">Launch with Parameter</a></p>
        </body>
    </html>
    

[](UnityasaLibrary.html)

Using Unity as a Library in other applications

[](XcodeFrameDebuggerIntegration.html)

Xcode frame debugger Unity integration

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

