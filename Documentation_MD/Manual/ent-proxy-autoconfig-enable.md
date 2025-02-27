[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ent-proxy-autoconfig-enable.html)
  * [中文](/cn/current/Manual/ent-proxy-autoconfig-enable.html)
  * [日本語](/ja/current/Manual/ent-proxy-autoconfig-enable.html)
  * [한국어](/kr/current/Manual/ent-proxy-autoconfig-enable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ent-proxy-autoconfig-enable.html)
  * [中文](/cn/current/Manual/ent-proxy-autoconfig-enable.html)
  * [日本語](/ja/current/Manual/ent-proxy-autoconfig-enable.html)
  * [한국어](/kr/current/Manual/ent-proxy-autoconfig-enable.html)

  * [Install and upgrade](install-and-upgrade.html)
  * [Deploy Unity across your enterprise](ent-deployment.html)
  * [Use Unity through web proxies](ent-proxy-autoconfig.html)
  * Enable automatic proxy configuration

[](ent-proxy-autoconfig.html)

Use Unity through web proxies

[](ent-proxy-autoconfig-store.html)

Store credentials for automatic proxy configuration (Windows)

# Enable automatic proxy configuration

If your environment is compatible with Unity’s automatic proxy configuration
feature, client computers must be configured to use it.

Review the solutions at [Using Unity through web proxies](ent-proxy-
autoconfig.html) to check if your environment supports Unity’s automatic proxy
configuration feature.

Whether you enable Unity’s automatic proxy configuration feature manually or
by using a more scalable method, configure client computers as follows:

  1. Check if the following directory exists on the client computer, and create it if it’s missing:

     * Windows: `C:\ProgramData\Unity\config`
     * macOS: `/Library/Application\ Support/Unity/config`
  2. Check if the directory in the previous step has a `services-config.json` file, and create it if it’s missing.

  3. Add the `"enableProxyAutoconfig"` key to the file and assign a value of `true`. If you’re creating the file, make sure it resembles the following example:
    
        {
        "enableProxyAutoconfig": true
    }
    

  4. Save the `services-config.json` file.

With automatic proxy configuration enabled, Unity applications will look for
stored user credentials on [Windows](ent-proxy-autoconfig-store.html) or
[macOS](ent-proxy-autoconfig-store-mac.html), if your organization’s web proxy
requires authentication. If the credentials aren’t stored or aren’t correct,
you’ll experience issues such as:

  * Project templates won’t be available in the Unity Hub when you create a new project.
  * Package Manager operations like searching or downloading packages will fail. In this case, the Editor displays error messages in the **Console window** A Unity Editor window that shows errors, warnings and other messages generated by Unity, or your own scripts. [More info](Console.html)  
See in [Glossary](Glossary.html#Consolewindow):

![Console errors after a failed proxy authentication](../uploads/Main/ent-
proxy-autoconfig-00.png) Console errors after a failed proxy authentication

## Next steps

  * If your organization set up its web proxy to require authentication, you need to store your credentials to authenticate with the web proxy. Refer to the following instructions: 
    * Windows: [Store credentials for automatic proxy configuration (Windows)](ent-proxy-autoconfig-store.html)
    * macOS: [Store credentials for automatic proxy configuration (macOS)](ent-proxy-autoconfig-store-mac.html)
  * Review the solutions in [Using Unity through web proxies](ent-proxy-autoconfig.html) to check if your environment requires any additional actions.

## Additional resources

  * [Solving network issues](upm-config-network.html) (Unity Package Manager)

[](ent-proxy-autoconfig.html)

Use Unity through web proxies

[](ent-proxy-autoconfig-store.html)

Store credentials for automatic proxy configuration (Windows)

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

