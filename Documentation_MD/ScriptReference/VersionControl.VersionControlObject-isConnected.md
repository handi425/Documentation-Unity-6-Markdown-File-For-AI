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

#
[VersionControlObject](VersionControl.VersionControlObject.html).isConnected

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

public bool isConnected;

### Description

Tests whether the
[VersionControlObject](VersionControl.VersionControlObject.html) is connected
to an underlying version control system.

There are various reasons why your VersionControlObject may not be connected.
For example:

  * Your VCS might need to be configured before establishing connection.
  * [OnActivate](VersionControl.VersionControlObject.OnActivate.html) might start a background thread that takes some time to connect.
  * The connection might get broken because of network issues.

In all these cases this property will return **false**.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.VersionControl;
    using UnityEngine;  
      
    [VersionControl("Custom")]
    public class CustomVersionControlObject : [VersionControlObject](VersionControl.VersionControlObject.html), [ISettingsInspectorExtension](VersionControl.ISettingsInspectorExtension.html)
    {
        bool m_Active;
        bool m_IsConnected;  
      
        public override bool isConnected => m_IsConnected;  
      
        public void OnEnable()
        {
            // m_Active will be false if CustomVersionControlObject has just been activated.
            // It will be true if OnEnable was called after domain reload. In that case we want to reestablish connection.
            if (m_Active)
                Connect();
        }  
      
        public void OnDisable()
        {
            // Let's assume that domain reload kills connection to underlying VCS.
            Disconnect();
        }  
      
        public override void OnActivate()
        {
            m_Active = true;
            // Let's try to automatically establish connection to underlying VCS.
            // It will not work the first time CustomVersionControlObject is activated because username is not configured yet.
            // However it will work on subsequent Unity startup.
            Connect();
        }  
      
        public override void OnDeactivate()
        {
            m_Active = false;
            Disconnect();
        }  
      
        public void OnInspectorGUI()
        {
            var oldUsername = EditorUserSettings.GetConfigValue("vcCustomUsername");
            var newUsername = [EditorGUILayout.TextField](EditorGUILayout.TextField.html)("Username (hint: TestUser):", oldUsername);
            if (newUsername != oldUsername)
                EditorUserSettings.SetConfigValue("vcCustomUsername", newUsername);  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Connected:", m_IsConnected ? "Yes" : "No");  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Connect"))
                Connect();
        }  
      
        void Connect()
        {
            var username = EditorUserSettings.GetConfigValue("vcCustomUsername");
            m_IsConnected = username == "TestUser";
        }  
      
        void Disconnect()
        {
            m_IsConnected = false;
        }
    }
    

Additional resources:
[VersionControlObject](VersionControl.VersionControlObject.html),
[ISettingsInspectorExtension](VersionControl.ISettingsInspectorExtension.html).

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

