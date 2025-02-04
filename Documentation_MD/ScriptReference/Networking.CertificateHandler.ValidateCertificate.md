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
[CertificateHandler](Networking.CertificateHandler.html).ValidateCertificate

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

protected bool ValidateCertificate(byte[] certificateData);

### Parameters

certificateData | Certificate data in PEM or DER format. If certificate data contains multiple certificates, the first one is the leaf certificate.  
---|---  
  
### Returns

**bool** `true` if the certificate should be accepted, `false` if not.

### Description

Callback, invoked for each leaf certificate sent by the remote server.

Override this to implement a custom certificate validation scheme.

    
    
    using UnityEngine.Networking;
    using System.Security.Cryptography.X509Certificates;  
      
    // Based on https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning#.Net
    class AcceptAllCertificatesSignedWithASpecificKeyPublicKey : [CertificateHandler](Networking.CertificateHandler.html)
    {
        // Encoded RSAPublicKey
        private static string PUB_KEY = "30818902818100C4A06B7B52F8D17DC1CCB47362" +
            "C64AB799AAE19E245A7559E9CEEC7D8AA4DF07CB0B21FDFD763C63A313A668FE9D764E" +
            "D913C51A676788DB62AF624F422C2F112C1316922AA5D37823CD9F43D1FC54513D14B2" +
            "9E36991F08A042C42EAAEEE5FE8E2CB10167174A359CEBF6FACC2C9CA933AD403137EE" +
            "2C3F4CBED9460129C72B0203010001";  
      
        protected override bool ValidateCertificate(byte[] certificateData)
        {
            X509Certificate2 certificate = new X509Certificate2(certificateData);
            string pk = certificate.GetPublicKeyString();
            if (pk.Equals(PUB_KEY))
                return true;  
      
            // Bad dog
            return false;
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

